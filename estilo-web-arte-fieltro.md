# Guía de Estilo Web: Arte en Fieltro Agujado (Needle Felting)

Este documento define la propuesta estética y la guía de diseño de interfaz (UI/UX) para un sitio web de artesanía y arte textil basado en la técnica de **fieltro agujado** (*needle felting* / lana vellón agüitada), inspirada en las obras analizadas (paisajes andinos, flora y fauna nativa como el bicho feo/turpial, cactus y figuras coyass).

---

## 1. Análises de la Técnica Artística

* **Técnica:** Fieltro agujado (*Needle Felting*) / Pintura con lana.
* **Textura:** Orgánica, fibrosa, suave, mates, con relieve tridimensional y bordes difuminados por la mezcla de las fibras de lana.
* **Temática:** Paisajes andinos, fauna silvestre, flora regional (cactus, cardones) y figuras culturales autóctonas.
* **Atmósfera:** Cálida, artesanal, acogedora, conectada con la tierra y la tradición hecha a mano (*handmade*).

---

## 2. Paleta de Colores

La paleta se extrae directamente de las lanas teñidas utilizadas en los cuadros:

| Uso | Tono / Nombre | Código HEX | Descripción |
| :--- | :--- | :--- | :--- |
| **Fondo Principal** | Blanco Lana / Crema | `#F7F5F0` | Un blanco cálido no purificado, simula el papel de hilo o base de vellón. |
| **Primario / Header** | Azul Cielo Andino | `#2B7C9E` | Tono azul verdoso mate, inspirado en el cielo abocetado en lana. |
| **Acento Verde** | Verde Cardón | `#3D784C` | Verde orgánico y desaturado presente en los cactus. |
| **Acento Calido** | Amarillo Flor de Cactus | `#E2A028` | Mostaza cálido que aporta destellos de luz. |
| **Acento Intenso** | Rojo Tusa / Tuna | `#9A2B43` | Magenta / borra de vino oscuro presente en los frutos de cactus. |
| **Texto Principal** | Carbón Téxtil | `#2D3132` | Gris muy oscuro para lectura fluida sin el contraste agresivo del negro puro. |
| **Fondo Secundario** | Arena de Cerros | `#EAE4D8` | Beige suave para contenedores, tarjetas y bloques destacados. |

---

## 3. Tipografía

Para transmitir la cualidad táctil y artesanal de la lana, se propone una combinación de tipografías redondeadas, humanas y serifas suaves:

* **Títulos Principales (H1, H2):** *Nunito* o *Quicksand* (Google Fonts)
  * *Características:* Tipografías *sans-serif* con terminaciones redondeadas (*rounded*), que imitan la suavidad de las fibras de lana sin perder legibilidad.
* **Cuerpos de Texto:** *Open Sans* o *Lato*
  * *Características:* Limpias, altamente legibles en pantallas digitales para descripciones, precios o artículos del taller.
* **Detalles / Frases Destacadas:** *Caveat* o *Amatic SC*
  * *Características:* Tipografía tipo manuscrita (*handwritten*) para simular etiquetas hechas a mano (como las tarjetas de cuidados de la obra).

---

## 4. UI Kit y Elementos Gráficos

### A. Botones y Contenedores (Cards)
* **Bordes Redondeados (*Border Radius*):** `16px` a `24px` para suavizar las esquinas.
* **Efecto Fieltro (CSS Box Shadows & Borders):**
  * Bordes suaves de `2px` con aspecto irregular o trazos sutiles.
  * Sombras difuminadas (`box-shadow: 0 8px 24px rgba(0,0,0,0.06)`) que den la impresión de que los elementos "flotan" como parches de fieltro sobre la superficie.

```css
/* Ejemplo de estilo para Tarjeta tipo Fieltro */
.card-fieltro {
  background-color: #ffffff;
  border-radius: 20px;
  border: 2px solid #EAE4D8;
  box-shadow: 0 10px 20px rgba(45, 49, 50, 0.05);
  padding: 24px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card-fieltro:hover {
  transform: translateY(-4px);
  box-shadow: 0 14px 28px rgba(45, 49, 50, 0.1);
}
```

### B. Botones Call-to-Action (CTA)
* **Botón Principal:**
  * Fondo `#2B7C9E` (Azul Cielo) o `#3D784C` (Verde Cardón).
  * Texto blanco, esquinas completamente redondeadas (`border-radius: 50px`).
* **Efecto Punteado:** Uso de bordes punteados (`border: 2px dashed #9A2B43`) en etiquetas o botones secundarios para emular las puntadas de costura o la textura de la aguja.

---

## 5. Estructura y Secciones del Sitio Web

1. **Navegación / Header:**
   * Textura suave de azul andino con menú limpio.
   * Logo con ícono de aguja de fieltrar o ovillo de lana.
2. **Hero Section (Inicio):**
   * Mensaje principal: *"La Textura de la Naturaleza en Fieltro"*.
   * Fondo con textura de vellón o galería de obras principales.
3. **Galería / Colecciones:**
   * Clasificación por temáticas: *Aves y Flora*, *Costumbres Andinas*, *Cuadros en Marco*.
   * Tarjetas con bordes suaves que resaltan las texturas de la lana al pasar el cursor (*hover*).
4. **Sección Taller / Proceso Creativo:**
   * Muestra del paso a paso (lana vellón, vellón peinado, agujas de fieltrar).
5. **Cuidados de la Obra (Ficha Técnica Interactiva):**
   * Inspirado en la etiqueta física adjunta en las obras:
     * *No exponer a luz solar directa prolongada.*
     * *No colgar en lugares con humedad.*
     * *Limpiar el vidrio por fuera con paño seco.*
6. **Footer / Pie de Página:**
   * Tono arena/tierra con enlaces rápidos, redes sociales y sello "Hecho a Mano con Pasión".

---

## 6. Recomendaciones de Texturas e Imágenes

* **Fotografía de Producto:** Las imágenes de las obras deben ser fotografiadas con luz natural indirecta para resaltar los relieves tridimensionales de la lana y la riqueza táctil de los colores.
* **Micro-interacciones:** Transiciones suaves (fadeIn, slideUp) que reflejen la ligereza y delicadeza de las fibras de lana.
