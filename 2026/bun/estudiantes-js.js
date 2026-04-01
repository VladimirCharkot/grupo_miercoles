function calcularPromedio(estudiante) {
  const suma = estudiante.calificaciones.reduce((acc, calificacion) => acc + calificacion, 0);
  return suma / estudiante.calificaciones.length;
}

const alicia = {
  nombre: "Alicia",
  edad: 20,
  calificaciones: [85, 90, 92, 88]
};

console.log(`El promedio de ${alicia.nombre} es: ${calcularPromedio(alicia)}`);