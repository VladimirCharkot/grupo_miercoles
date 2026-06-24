export {};

/**
 * Ejercicios de Higher Order Functions (HOFs) en TypeScript
 *
 * Temas: filter, map, sort, reduce, y promesas con sleep/probabilidad
 *
 * Para correr: bun ejercicios-hof.ts
 */

// ===========================================================================
// DATOS DE EJEMPLO
// ===========================================================================

type Producto = {
  nombre: string;
  precio: number;
  categoria: string;
  stock: number;
};

const productos: Producto[] = [
  { nombre: "Medialunas", precio: 1200, categoria: "panadería", stock: 50 },
  { nombre: "Facturas", precio: 1500, categoria: "panadería", stock: 30 },
  { nombre: "Mate", precio: 8000, categoria: "bebida", stock: 10 },
  { nombre: "Yerba", precio: 4500, categoria: "bebida", stock: 25 },
  { nombre: "Dulce de leche", precio: 3200, categoria: "lácteo", stock: 0 },
  { nombre: "Queso cremoso", precio: 5600, categoria: "lácteo", stock: 8 },
  { nombre: "Alfajor triple", precio: 2100, categoria: "kiosco", stock: 100 },
  { nombre: "Gaseosa", precio: 1800, categoria: "bebida", stock: 15 },
];

// ===========================================================================
// FILTER
// ===========================================================================

/**
 * Ejercicio 1 — filter básico
 *
 * Quedarse solo con los productos que tienen stock disponible.
 * filter recibe una función predicado: si devuelve true, el elemento se incluye.
 */
const conStock = productos.filter((p) => p.stock > 0);
console.log("Con stock:", conStock.map((p) => p.nombre));

/**
 * Ejercicio 2 — filter con múltiples condiciones
 *
 * Productos de panadería que cuestan menos de $1400.
 * Se pueden encadenar condiciones con && adentro del predicado.
 */
const baratosYPan = productos.filter(
  (p) => p.categoria === "panadería" && p.precio < 1400
);
console.log("Baratos y de panadería:", baratosYPan.map((p) => p.nombre));

/**
 * Ejercicio 3 — filter + índice
 *
 * filter también recibe el índice como segundo argumento.
 * Acá nos quedamos solo con los productos en posición par del array.
 */
const enPosicionPar = productos.filter((_, i) => i % 2 === 0);
console.log("Posiciones pares:", enPosicionPar.map((p) => p.nombre));

// ===========================================================================
// MAP
// ===========================================================================

/**
 * Ejercicio 4 — map básico
 *
 * map transforma cada elemento y devuelve un array nuevo del mismo largo.
 * Acá convertimos cada producto en un string con formato de ticket.
 */
const ticket = productos.map(
  (p) => `${p.nombre.padEnd(20)} $${p.precio.toLocaleString("es-AR")}`
);
console.log("\nTicket:\n" + ticket.join("\n"));

/**
 * Ejercicio 5 — map para transformar la forma del objeto
 *
 * A veces necesitamos agarrar algunos campos y armar un objeto nuevo.
 * Esto se llama "proyección" y es re común cuando trabajás con APIs.
 */
const resumen = productos.map(({ nombre, precio }) => ({ nombre, precio }));
console.log("\nResumen (solo nombre y precio):", resumen);

/**
 * Ejercicio 6 — map para aplicar un descuento
 *
 * Aplicar 15% de descuento a todos los productos de bebida.
 * Importante: map no muta el array original, devuelve uno nuevo.
 */
const conDescuento = productos.map((p) =>
  p.categoria === "bebida"
    ? { ...p, precio: Math.round(p.precio * 0.85) }
    : p
);
console.log(
  "\nPrecios bebidas con descuento:",
  conDescuento
    .filter((p) => p.categoria === "bebida")
    .map((p) => `${p.nombre}: $${p.precio}`)
);

// ===========================================================================
// SORT
// ===========================================================================

/**
 * Ejercicio 7 — sort por precio ascendente
 *
 * sort recibe una función comparadora: si devuelve negativo, a va antes que b.
 * CUIDADO: sort muta el array original. Usamos [...arr] para clonar primero.
 */
const porPrecioAsc = [...productos].sort((a, b) => a.precio - b.precio);
console.log(
  "\nPor precio (menor a mayor):",
  porPrecioAsc.map((p) => `${p.nombre} $${p.precio}`)
);

/**
 * Ejercicio 8 — sort alfabético
 *
 * Para strings usamos localeCompare, que maneja bien los acentos y la ñ.
 */
const alfabetico = [...productos].sort((a, b) =>
  a.nombre.localeCompare(b.nombre, "es-AR")
);
console.log("\nAlfabético:", alfabetico.map((p) => p.nombre));

/**
 * Ejercicio 9 — sort con criterio múltiple
 *
 * Primero ordenar por categoría, y si son iguales, por precio descendente.
 * Se puede encadenar la lógica con || corto-circuito.
 */
const porCategoriaYPrecio = [...productos].sort(
  (a, b) =>
    a.categoria.localeCompare(b.categoria, "es-AR") ||
    b.precio - a.precio // si localeCompare devuelve 0, evalúa esto
);
console.log(
  "\nPor categoría y precio desc:",
  porCategoriaYPrecio.map((p) => `[${p.categoria}] ${p.nombre} $${p.precio}`)
);

// ===========================================================================
// REDUCE
// ===========================================================================

/**
 * Ejercicio 10 — reduce para sumar
 *
 * reduce "acumula" un valor recorriendo el array.
 * El segundo argumento de reduce es el valor inicial del acumulador.
 */
const totalStock = productos.reduce((acc, p) => acc + p.stock, 0);
console.log("\nTotal de unidades en stock:", totalStock);

/**
 * Ejercicio 11 — reduce para agrupar
 *
 * Una de las uses más copadas de reduce: agrupar por categoría.
 * El acumulador arranca como objeto vacío y vamos agregando claves.
 */
const porCategoria = productos.reduce<Record<string, Producto[]>>(
  (acc, p) => {
    // Si la categoría no existe en el acumulador, la inicializamos
    if (!acc[p.categoria]) acc[p.categoria] = [];
    acc[p.categoria].push(p);
    return acc;
  },
  {}
);
console.log("\nAgrupado por categoría:", Object.keys(porCategoria));

/**
 * Ejercicio 12 — reduce para calcular estadísticas
 *
 * En un solo recorrido obtenemos el total, mínimo y máximo.
 */
const stats = productos.reduce(
  (acc, p) => ({
    total: acc.total + p.precio,
    min: Math.min(acc.min, p.precio),
    max: Math.max(acc.max, p.precio),
  }),
  { total: 0, min: Infinity, max: -Infinity }
);
console.log(
  `\nEstadísticas de precio — total: $${stats.total}, min: $${stats.min}, max: $${stats.max}`
);

// ===========================================================================
// PROMESAS — SLEEP + PROBABILIDAD
// ===========================================================================

/**
 * Espera `ms` milisegundos y después resuelve.
 * Es la versión promisificada del setTimeout de toda la vida.
 */
const sleep = (ms: number): Promise<void> =>
  new Promise((resolve) => setTimeout(resolve, ms));

/**
 * Ejercicio 13 — promesa con probabilidad de falla
 *
 * Simula una operación que puede fallar, como un llamado a una API chabona.
 * `chanceDeExito` es un número entre 0 y 1 (ej: 0.7 = 70% de éxito).
 */
const operacionInestable = (
  nombre: string,
  chanceDeExito: number,
  demora: number
): Promise<string> => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const salio = Math.random() < chanceDeExito;
      if (salio) {
        resolve(`✓ "${nombre}" completada`);
      } else {
        reject(new Error(`✗ "${nombre}" falló (mala suerte, amigo)`));
      }
    }, demora);
  });
};

/**
 * Ejercicio 14 — encadenar promesas con .then / .catch
 *
 * El .then se ejecuta si la promesa resolvió bien.
 * El .catch atrapa cualquier error que haya tirado la cadena.
 */
console.log("\n--- Ejercicio 14: then/catch ---");
operacionInestable("consulta a la BD", 0.7, 500)
  .then((msg) => {
    console.log(msg);
    // Podemos encadenar otra operación que depende del resultado anterior
    return operacionInestable("guardar resultado", 0.8, 300);
  })
  .then((msg) => console.log(msg))
  .catch((err) => console.error("Error en la cadena:", err.message));

/**
 * Ejercicio 15 — async/await (azúcar sintáctica para then/catch)
 *
 * Es exactamente lo mismo que el ejercicio anterior pero más legible.
 * El try/catch reemplaza al .catch.
 */
const correrOperaciones = async () => {
  console.log("\n--- Ejercicio 15: async/await ---");
  try {
    // Esperamos que termine antes de seguir
    const r1 = await operacionInestable("login", 0.75, 400);
    console.log(r1);

    await sleep(200); // pausa artificial entre pasos

    const r2 = await operacionInestable("cargar perfil", 0.9, 300);
    console.log(r2);
  } catch (err) {
    // Si cualquiera de las dos falla, cae acá
    console.error("Algo explotó:", (err as Error).message);
  }
};

/**
 * Ejercicio 16 — Promise.all: correr varias promesas en paralelo
 *
 * En vez de esperar una por una, las lanzamos todas juntas.
 * Si CUALQUIERA falla, Promise.all rechaza inmediatamente.
 */
const correrEnParalelo = async () => {
  console.log("\n--- Ejercicio 16: Promise.all ---");
  try {
    const resultados = await Promise.all([
      operacionInestable("servicio A", 0.8, 600),
      operacionInestable("servicio B", 0.8, 400),
      operacionInestable("servicio C", 0.8, 500),
    ]);
    console.log("Todos salieron bien:", resultados);
  } catch (err) {
    console.error("Al menos uno falló:", (err as Error).message);
  }
};

/**
 * Ejercicio 17 — Promise.allSettled: correr sin importar si alguno falla
 *
 * A diferencia de Promise.all, este espera a todos y te dice el resultado
 * de cada uno individualmente. Ideal cuando querés reintentar solo los que fallaron.
 */
const correrSinMiedo = async () => {
  console.log("\n--- Ejercicio 17: Promise.allSettled ---");
  const resultados = await Promise.allSettled([
    operacionInestable("microservicio 1", 0.6, 300),
    operacionInestable("microservicio 2", 0.6, 500),
    operacionInestable("microservicio 3", 0.6, 200),
  ]);

  resultados.forEach((r, i) => {
    if (r.status === "fulfilled") {
      console.log(`Servicio ${i + 1} OK:`, r.value);
    } else {
      console.log(`Servicio ${i + 1} falló:`, r.reason.message);
    }
  });
};

// Correr todos los ejercicios async en secuencia
await correrOperaciones();
await correrEnParalelo();
await correrSinMiedo();
