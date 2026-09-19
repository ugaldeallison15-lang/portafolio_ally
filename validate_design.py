import yaml
import re
from pathlib import Path

# Load the DESIGN.md file
with open('/Users/allisonugalde/Desktop/ltei-grupo-2/DESIGN.md', 'r') as f:
    content = f.read()

# Extract front matter (YAML between ---)
front_matter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
if front_matter_match:
    yaml_content = front_matter_match.group(1)
    tokens = yaml.safe_load(yaml_content)
else:
    tokens = {}

# Helper: Convert hex to RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Helper: Calculate relative luminance
def relative_luminance(rgb):
    def normalize(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = [normalize(c) for c in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

# Helper: Calculate contrast ratio
def contrast_ratio(color1, color2):
    l1 = relative_luminance(hex_to_rgb(color1))
    l2 = relative_luminance(hex_to_rgb(color2))
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

# 1. STRUCTURE VALIDATION
print("=" * 60)
print("VALIDACIÓN DE ESTRUCTURA (design.md)")
print("=" * 60)

required_sections = ['colors', 'typography', 'spacing', 'rounded', 'components']
required_prose_sections = [
    'Overview', 'Colors', 'Typography', 'Layout', 
    'Elevation & Depth', 'Shapes', 'Components', 'Do\'s and Don\'ts'
]

structure_ok = True

# Check front matter sections
for section in required_sections:
    if section in tokens:
        print(f"✅ Front matter: sección '{section}' presente")
    else:
        print(f"❌ Front matter: FALTA sección '{section}'")
        structure_ok = False

# Check prose sections
for section in required_prose_sections:
    pattern = rf'^# {re.escape(section)}'
    if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
        print(f"✅ Prosa: sección '{section}' presente")
    else:
        print(f"❌ Prosa: FALTA sección '{section}'")
        structure_ok = False

# Check token references in prose
token_refs = re.findall(r'\{([^}]+)\}', content)
print(f"\n📌 Referencias a tokens encontradas en prosa: {len(token_refs)}")

# 2. COLOR CONTRAST ANALYSIS (WCAG AA 4.5:1)
print("\n" + "=" * 60)
print("ANÁLISIS DE CONTRASTE (WCAG AA 4.5:1)")
print("=" * 60)

colors = tokens.get('colors', {})

# Define text/background pairs to check based on components
pairs_to_check = [
    # (name, text_color, bg_color, min_ratio)
    ("Botón primario: texto vs fondo", colors['background'], colors['primary']),
    ("Botón secundario: texto vs fondo", colors['primary'], colors['background']),
    ("Botón secundario hover: texto vs fondo", colors['background'], colors['primary']),
    ("Botón ícono: texto vs fondo", colors['background'], colors['secondary']),
    ("Enlace principal: texto vs fondo blanco", colors['primary'], colors['background']),
    ("Enlace hover: texto vs fondo blanco", colors['secondary'], colors['background']),
    ("Texto principal: vs fondo blanco", colors['text'], colors['background']),
    ("Texto principal: vs fondo cálido", colors['text'], colors['backgroundWarm']),
    ("Texto secundario: vs fondo blanco", colors['textSecondary'], colors['background']),
    ("Texto secundario: vs fondo cálido", colors['textSecondary'], colors['backgroundWarm']),
    ("Input texto: vs fondo", colors['text'], colors['background']),
    ("Input placeholder/aux: vs fondo", colors['textSecondary'], colors['background']),
    ("Social icon normal: icono vs fondo", colors['primary'], colors['background']),
    ("Social icon hover: icono vs fondo", colors['background'], colors['secondary']),
    ("Card contenido: texto vs fondo cálido", colors['text'], colors['backgroundWarm']),
    ("Estrella rosa: vs fondo blanco", colors['secondary'], colors['background']),
    ("Estrella azul: vs fondo blanco", colors['primary'], colors['background']),
    ("Borde input: vs fondo", colors['border'], colors['background']),
    ("Borde focus: vs fondo", colors['borderFocus'], colors['background']),
]

contrast_issues = []
for name, text_c, bg_c in pairs_to_check:
    ratio = contrast_ratio(text_c, bg_c)
    passes = ratio >= 4.5
    status = "✅" if passes else "❌"
    if not passes:
        contrast_issues.append((name, text_c, bg_c, ratio))
    print(f"{status} {name}: {ratio:.2f}:1 {'(FALLA)' if not passes else ''}")

# 3. UNUSED COLORS DETECTION
print("\n" + "=" * 60)
print("COLORES DEFINIDOS PERO NO USADOS")
print("=" * 60)

# Collect all color references in components
used_colors = set()

def extract_color_refs(obj, prefix=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            extract_color_refs(v, f"{prefix}.{k}" if prefix else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            extract_color_refs(v, f"{prefix}[{i}]")
    elif isinstance(obj, str):
        # Find {colors.xxx} references
        refs = re.findall(r'\{colors\.([^}]+)\}', obj)
        for ref in refs:
            used_colors.add(ref)

extract_color_refs(tokens.get('components', {}))

# Also check prose for color references
prose_color_refs = re.findall(r'\{colors\.([^}]+)\}', content)
for ref in prose_color_refs:
    used_colors.add(ref)

defined_colors = set(colors.keys())
unused_colors = defined_colors - used_colors

if unused_colors:
    print("⚠️  Colores definidos pero NO referenciados en components ni prosa:")
    for color in sorted(unused_colors):
        print(f"   - colors.{color} = {colors[color]}")
else:
    print("✅ Todos los colores definidos se usan en components o prosa")

# Also check for colors referenced but not defined
referenced_but_undefined = used_colors - defined_colors
if referenced_but_undefined:
    print("\n⚠️  Colores referenciados pero NO definidos:")
    for color in sorted(referenced_but_undefined):
        print(f"   - colors.{color}")

# Summary
print("\n" + "=" * 60)
print("RESUMEN")
print("=" * 60)
print(f"Estructura: {'✅ OK' if structure_ok else '❌ PROBLEMAS'}")
print(f"Contraste: {'✅ Todo pasa WCAG AA' if not contrast_issues else f'❌ {len(contrast_issues)} pares fallan'}")
print(f"Colores no usados: {'✅ Ninguno' if not unused_colors else f'⚠️ {len(unused_colors)} colores'}")
