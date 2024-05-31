const fs = require("fs");
const path = require("path");
const express = require("express");
const bp = require("body-parser");
const MarkdownIt = require("markdown-it");
const md = new MarkdownIt();

const app = express();

app.use(express.static("pub"));
app.use(bp.json());
app.use(bp.urlencoded({ extended: true }));

app.listen(3000, () => {
  console.log("Servidor iniciado");
});

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.post("/", (req, res) => {
  console.log(req.body);
  let markdownText = req.body.text;
  console.log(markdownText);
  let htmlText = md.render(markdownText);
  response.setHeader("Content-Type", "aplication/json");
  response.end(JSON.stringify({ 
    text: htmlText 
  }));
});
