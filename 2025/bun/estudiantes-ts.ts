interface Estudiante {
  nombre: string;
  edad: number;
  calificaciones: [number, number, number];
}

function calcularPromedio(estudiante: Estudiante): number {
  const suma = estudiante.calificaciones.reduce((acc, calificacion) => acc + calificacion, 0);
  return suma / estudiante.calificaciones.length;
}

const alicia: Estudiante = {
  nombre: "Alicia",
  edad: 20,
  calificaciones: [85, 90, 92]
};

const carlos: Estudiante = {
  nombre: 'Carlos',
  edad: alicia.calificaciones[0],
  calificaciones: [97, 89, 91]
}

console.log(`El promedio de ${alicia.nombre} es: ${calcularPromedio(alicia)}`);
console.log(`El promedio de ${carlos.nombre} es: ${calcularPromedio(carlos)}`);