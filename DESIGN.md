---
colors:
  primary: "#3155A6"
  primaryHover: "#274488"
  primaryLight: "#7EA6D8"
  secondary: "#C02D6E"
  secondaryHover: "#A0255A"
  secondaryLight: "#F3A6C4"
  background: "#FFFFFF"
  backgroundWarm: "#FAF8F6"
  text: "#3155A6"
  textSecondary: "#4A4A4A"
  border: "#3155A6"
  borderFocus: "#C02D6E"
typography:
  fontFamilyPrimary: "Hobeaux Bold"
  fontFamilySecondary: "Avenir"
  fontSizeDisplay: "48px"
  fontSizeHeading: "32px"
  fontSizeSubheading: "20px"
  fontSizeBody: "16px"
  fontSizeSmall: "14px"
  fontWeightBold: 700
  fontWeightMedium: 500
  fontWeightRegular: 400
  lineHeightTight: 1.2
  lineHeightNormal: 1.5
  lineHeightRelaxed: 1.6
spacing:
  xs: "8px"
  sm: "16px"
  md: "24px"
  lg: "32px"
  xl: "48px"
  xxl: "64px"
size:
  icon: "32px"
rounded:
  sm: "8px"
  md: "12px"
  lg: "20px"
  xl: "24px"
  full: "9999px"
components:
  button:
    primary:
      background: "{colors.primary}"
      color: "{colors.background}"
      borderRadius: "{rounded.md}"
      fontFamily: "{typography.fontFamilySecondary}"
      fontSize: "{typography.fontSizeBody}"
      fontWeight: "{typography.fontWeightMedium}"
    secondary:
      background: "{colors.background}"
      color: "{colors.primary}"
      border: "1px solid {colors.primary}"
      borderRadius: "{rounded.md}"
      fontFamily: "{typography.fontFamilySecondary}"
      fontSize: "{typography.fontSizeBody}"
      fontWeight: "{typography.fontWeightMedium}"
    icon:
      background: "{colors.secondary}"
      color: "{colors.background}"
      borderRadius: "{rounded.full}"
      size: "{size.icon}"
  card:
    background: "{colors.backgroundWarm}"
    border: "1px solid {colors.border}"
    borderRadius: "{rounded.md}"
    padding: "{spacing.md}"
  input:
    background: "{colors.background}"
    border: "1px solid {colors.border}"
    borderRadius: "{rounded.md}"
    fontFamily: "{typography.fontFamilySecondary}"
    fontSize: "{typography.fontSizeBody}"
    color: "{colors.text}"
  link:
    color: "{colors.primary}"
    hoverColor: "{colors.secondary}"
    fontFamily: "{typography.fontFamilySecondary}"
    fontSize: "{typography.fontSizeBody}"
    fontWeight: "{typography.fontWeightMedium}"
  socialIcon:
    size: "{size.icon}"
    borderRadius: "{rounded.full}"
    background: "{colors.background}"
    color: "{colors.primary}"
    hoverBackground: "{colors.secondary}"
    hoverColor: "{colors.background}"
  star:
    colors: ["{colors.secondary}", "{colors.primary}", "{colors.secondaryLight}"]
    usage: "accent"
---

# Overview

Mi sistema de diseño refleja una personalidad **creativa, alegre y cercana**. Busco que mi trabajo se sienta cuidado y profesional, pero nunca demasiado serio. Hay una parte espontánea y divertida que forma parte de mi manera de diseñar: disfruto el color, los detalles inesperados y las propuestas que tienen algo que decir.

Mi identidad parte de una base **azul, blanco y rosa**, que transmite confianza y calidez. El rosa aparece con un contraste para representar esa parte más atrevida y expresiva, funcionando como color de personalidad y reconocimiento.

---

# Colors

Mi paleta busca reflejar una personalidad **creativa, segura, alegre y cercana**. Cada color tiene un rol definido:

| Token | Valor | Rol | Uso |
|-------|-------|-----|-----|
| `colors.primary` | `#3155A6` | Confianza y seguridad | Títulos, elementos principales, piezas que requieren profesionalismo |
| `colors.primaryHover` | `#274488` | Interacción | Estados hover de botones primarios |
| `colors.primaryLight` | `#7EA6D8` | Frescura | Fondos, gráficos, elementos secundarios, bordes sutiles |
| `colors.secondary` | `#C02D6E` | Creatividad y personalidad | Acentos, detalles, palabras clave, elementos destacados, botones de ícono |
| `colors.secondaryHover` | `#A0255A` | Interacción | Estados hover de acentos |
| `colors.secondaryLight` | `#F3A6C4` | Cercanía y feminidad | Fondos alternativos (tarjetas), detalles decorativos, estrellas |
| `colors.background` | `#FFFFFF` | Claridad y equilibrio | Base neutra, fondos principales |
| `colors.backgroundWarm` | `#FAF8F6` | Calidez orgánica | Fondos alternativos para estética más cercana, tarjetas |
| `colors.text` | `#3155A6` | Texto principal | Títulos, cuerpo de texto |
| `colors.textSecondary` | `#4A4A4A` | Texto secundario | Textos auxiliares, descripciones |
| `colors.border` | `#3155A6` | Bordes sutiles | Campos, contenedores |
| `colors.borderFocus` | `#C02D6E` | Foco/Activo | Bordes en estado activo, interacción |

**Intención de la paleta:**
- **Azul principal** (`#3155A6`): confianza y seguridad
- **Rosa mexicano** (`#C02D6E`): creatividad y personalidad (oscurecido para accesibilidad)
- **Azul claro** (`#7EA6D8`): frescura — *solo fondos/gráficos, no texto ni bordes*
- **Rosa suave** (`#F3A6C4`): cercanía y feminidad — fondos alternativos, detalles decorativos
- **Blanco** (`#FFFFFF`): claridad y equilibrio
- **Blanco cálido** (`#FAF8F6`): cercanía y organicidad
- **Gris neutro** (`#4A4A4A`): texto secundario, placeholders, descripciones (WCAG AA)

---

# Typography

Mi sistema tipográfico equilibra **expresión y claridad**. Combino una tipografía con mayor personalidad para los títulos (`Hobeaux Bold`) con una sans serif limpia para la información (`Avenir`), creando una identidad visual creativa, cercana y fácil de reconocer.

## Familias tipográficas

| Token | Valor | Uso |
|-------|-------|-----|
| `typography.fontFamilyPrimary` | `Hobeaux Bold` | Títulos, nombres de proyectos, frases destacadas, elementos con presencia visual |
| `typography.fontFamilySecondary` | `Avenir` | Subtítulos, textos, navegación, botones, enlaces, contenido general |

## Jerarquía tipográfica

| Nivel | Familia | Tamaño | Peso | Token de referencia |
|-------|---------|--------|------|---------------------|
| Título principal | Hobeaux Bold | 48px | Bold | `typography.fontSizeDisplay`, `typography.fontWeightBold` |
| Título de sección | Hobeaux Bold | 32px | Bold | `typography.fontSizeHeading`, `typography.fontWeightBold` |
| Subtítulo | Avenir | 20px | Medium | `typography.fontSizeSubheading`, `typography.fontWeightMedium` |
| Cuerpo de texto | Avenir | 16px | Regular | `typography.fontSizeBody`, `typography.fontWeightRegular` |
| Texto destacado | Avenir | 16px | Bold | `typography.fontSizeBody`, `typography.fontWeightBold` |
| Texto pequeño | Avenir | 14px | Regular | `typography.fontSizeSmall`, `typography.fontWeightRegular` |
| Botones | Avenir | 16px | Medium | `typography.fontSizeBody`, `typography.fontWeightMedium` |
| Enlaces | Avenir | 16px | Medium | `typography.fontSizeBody`, `typography.fontWeightMedium` |

La jerarquía se construye mediante **tamaño, peso y contraste** entre ambas tipografías. `Hobeaux Bold` aporta personalidad y expresión; `Avenir` genera equilibrio y legibilidad. Juntas crean una voz visual reconocible, creativa y profesional.

---

# Layout

Mi composición mantiene un **equilibrio entre orden y libertad creativa**. Utilizo el espacio para darle protagonismo a cada proyecto y evitar que los elementos compitan entre sí, sin limitarme a estructuras completamente rígidas.

## Espaciado

Trabajo con una **base de 8px** para consistencia en márgenes, separaciones y tamaños:

| Token | Valor | Uso |
|-------|-------|-----|
| `spacing.base` / `spacing.xs` | 8px | Espaciado mínimo, separación entre elementos relacionados |
| `spacing.sm` | 16px | Separación entre componentes, padding interno |
| `spacing.md` | 24px | Separación entre secciones, padding de tarjetas |
| `spacing.lg` | 32px | Separación mayor entre bloques |
| `spacing.xl` | 48px | Separación de secciones principales |
| `spacing.xxl` | 64px | Separación máxima, hero sections |

## Retícula y composición

- **Escritorio**: retícula de **12 columnas**
- **Tableta**: reducción progresiva de columnas (8-6)
- **Móvil**: **1 columna**, priorizando lectura y navegación

El **espacio en blanco** es parte fundamental de la identidad: genera pausas visuales, destaca elementos y hace que las composiciones se sientan limpias, frescas y equilibradas.

---

# Elevation & Depth

Mi sistema de profundidad es **sutil y contemporáneo**. La mayor parte de los elementos se mantienen **planos** para que el color, la tipografía y la composición sean protagonistas.

## Principios

- Sombras **ligeras únicamente** para diferenciar elementos, generar separación o indicar interacción
- **Profundidad suave** antes que efectos marcados
- Estética **ligera y cercana**

## Aplicación

| Elemento | Elevación |
|----------|-----------|
| Tarjetas, imágenes, elementos destacados | Elevación discreta (`box-shadow` sutil) para crear jerarquía |
| Elementos interactivos (botones, enlaces) | Cambio de sombra o posición al hover/active para reforzar respuesta |
| Fondos y elementos planos | Sin sombra (planos) |

La profundidad **organiza la información y da ritmo** sin quitar protagonismo al contenido.

---

# Shapes

Mis formas combinan **estructuras geométricas con bordes suaves** para una estética equilibrada entre lo ordenado y lo creativo.

## Radios de borde

| Token | Valor | Uso |
|-------|-------|-----|
| `rounded.sm` | 8px | Elementos pequeños, chips, badges |
| `rounded.md` | 12px | **Predominante**: botones, tarjetas, contenedores, campos, formularios |
| `rounded.lg` | 20px | Elementos visuales destacados |
| `rounded.xl` | 24px | Elementos visuales destacados grandes |
| `rounded.full` | 9999px | Botones de ícono, avatares, íconos sociales |

## Formas geométricas y orgánicas

- **Círculos**: fotografías de perfil, íconos, pequeños elementos gráficos, botones de ícono (32×32px), íconos sociales
- **Geométricas**: círculos, líneas, bloques de color para generar ritmo y composiciones dinámicas
- **Orgánicas/irregulares**: uso **puntual** como recurso expresivo para aportar espontaneidad y diferenciar piezas sin perder coherencia

Las formas funcionan como herramientas para **organizar, destacar y dar personalidad**, complementando la paleta sin sobrecargar.

---

# Components

Los componentes mantienen una apariencia **limpia, cercana y creativa**. El azul (`{colors.primary}`) funciona como color principal; el rosa mexicano (`{colors.secondary}`, oscurecido a `#C02D6E` para accesibilidad) como acento.

## Botones

### Primario (`components.button.primary`)
- Fondo: `{colors.primary}`
- Texto: `{colors.background}` (blanco)
- Tipografía: `{typography.fontFamilySecondary}`, `{typography.fontSizeBody}`, `{typography.fontWeightMedium}`
- Bordes: `{rounded.md}` (12px)
- Hover: cambio de tono a `{colors.primaryHover}` o sombra ligera

### Secundario (`components.button.secondary`)
- Fondo: `{colors.background}` (blanco)
- Borde: 1px solid `{colors.primary}`
- Texto: `{colors.primary}`
- Tipografía: misma que primario
- Bordes: `{rounded.md}` (12px)
- Hover: fondo `{colors.primary}`, texto `{colors.background}`

### De ícono (`components.button.icon`)
- Circular: `{rounded.full}`
- Fondo principal: `{colors.secondary}` (rosa mexicano accesible `#C02D6E`)
- Tamaño: 32×32px
- Hover: `{colors.secondaryHover}` (`#A0255A`)

## Tarjetas y contenedores (`components.card`)
- Fondo: `{colors.backgroundWarm}` o `{colors.secondaryLight}` (rosa suave) para variantes cálidas
- Bordes: 1px solid `{colors.border}` (sutiles, azul principal)
- Bordes redondeados: `{rounded.md}` (12px)
- Padding: `{spacing.md}` (24px)
- Contenido limpio para que imágenes/proyectos sean protagonistas

## Campos y formularios (`components.input`)
- Fondo: `{colors.background}`
- Texto: `{typography.fontFamilySecondary}`, `{typography.fontSizeBody}`, `{colors.text}`
- Bordes: 1px solid `{colors.border}` (`{colors.primary}`)
- Bordes redondeados: `{rounded.md}` (12px)
- **Estado activo**: borde cambia a `{colors.primary}` o `{colors.borderFocus}` (`{colors.secondary}`)
- Textos auxiliares: tonos neutros (`{colors.textSecondary}`)

## Navegación y enlaces (`components.link`)
- Tipografía: `{typography.fontFamilySecondary}`, `{typography.fontSizeBody}`, `{typography.fontWeightMedium}`
- Color principal: `{colors.primary}`
- Hover/Activo: `{colors.secondary}` (rosa mexicano)
- Cambio de color = señal visual de interacción (sin efectos excesivos)

## Íconos sociales (`components.socialIcon`)
- Contenedor circular: 32×32px (`{rounded.full}`)
- Estado normal: fondo `{colors.background}`, color `{colors.primary}` (azul)
- Hover/Interacción: fondo `{colors.secondary}` (rosa mexicano `#C02D6E`), color `{colors.background}` (blanco)

## Estrellas (`components.star`)
- **Recurso gráfico distintivo** de la identidad
- Colores: `{colors.secondary}` (rosa mexicano), `{colors.primary}` (azul) y `{colors.secondaryLight}` (rosa suave)
- Uso: **intencional y moderado** como acentos visuales
- Funciones: acompañar títulos, destacar información, señalar elementos importantes, generar ritmo
- Aportan: dinamismo, personalidad, detalle espontáneo y expresivo

---

# Do's and Don'ts

## Do's ✅

- **Usa el azul** (`{colors.primary}` `#3155A6`) como color principal para construir una base visual equilibrada y profesional
- **Utiliza el rosa mexicano** (`{colors.secondary}` `#C02D6E`) como acento para destacar elementos importantes y aportar personalidad (cumple WCAG AA sobre blanco)
- **Mantén el blanco** (`{colors.background}` / `{colors.backgroundWarm}`) como espacio de descanso visual para evitar composiciones saturadas
- **Combina `Hobeaux Bold` en títulos con `Avenir`** para textos y elementos funcionales
- **Utiliza las estrellas** (`components.star`) como recurso gráfico distintivo, especialmente para acompañar títulos, destacar información o generar ritmo visual (colores: `{colors.secondary}`, `{colors.primary}`, `{colors.secondaryLight}`)
- **Mantén las formas redondeadas** (`{rounded.md}` predominante) y los elementos gráficos consistentes con la identidad
- **Permite que cada proyecto tenga cierta libertad visual**, siempre respetando la paleta, tipografía y recursos gráficos de la marca
- **Prioriza composiciones claras** donde el contenido tenga suficiente espacio (`{spacing.md}`+) para destacar
- **Usa gris neutro** (`{colors.textSecondary}` `#4A4A4A`) para textos secundarios, placeholders y descripciones (garantiza contraste)
- **Usa azul principal** (`{colors.border}` `#3155A6`) para bordes de campos y estados focus (accesible)

## Don'ts ❌

- **No utilices demasiados colores** fuera de la paleta principal (`colors.*`)
- **No satures las composiciones** utilizando rosa mexicano (`{colors.secondary}`) en grandes cantidades
- **No combines demasiados estilos tipográficos** dentro de una misma pieza (máx. 2 familias: `fontFamilyPrimary` + `fontFamilySecondary`)
- **No utilices las estrellas** o recursos gráficos de manera excesiva; deben funcionar como **acentos**, no como decoración constante
- **No llenes los espacios vacíos** únicamente por evitar que una composición se vea "vacía" (respeta `spacing.*`)
- **No utilices sombras, efectos o degradados** que hagan que la identidad pierda su apariencia limpia (usa elevación sutil únicamente)
- **No hagas que todos los proyectos se vean exactamente iguales**; la identidad debe dar unidad sin limitar la creatividad
- **No sacrifiques la legibilidad** por hacer una composición más llamativa (respeta `typography.*` jerarquía y `spacing.*`)
- **No uses azul claro** (`{colors.primaryLight}` `#7EA6D8`) **como texto ni bordes** — solo fondos/gráficos (falla WCAG AA)
- **No uses rosa suave** (`{colors.secondaryLight}` `#F3A6C4`) **como texto** — solo fondos decorativos