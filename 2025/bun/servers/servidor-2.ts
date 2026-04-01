const server = Bun.serve({
  port: 3333,
  fetch: (req) => {
    const url = new URL(req.url);

    if (url.pathname === "/") {
      return new Response("Hola :D");
      // return new Response("<html><head></head><body><h1>Holaaa :D</h1></body></html>", { headers: { "Content-Type": "text/html" } });
    }

    if (url.pathname === "/hora") {
      return Response.json({
        hora: new Date().toISOString()
      });
    }

    return new Response("Not Found", { status: 404 });
  },
});

console.log(`Servidor corriendo en http://localhost:${server.port}!`);