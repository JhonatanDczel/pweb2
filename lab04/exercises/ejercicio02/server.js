const fs = require("fs");
const path = require("path");
const express = require("express");
const app = express();
app.use(express.static("pub"));

app.listen(3000, () => {
  console.log("Server started on http://localhost:3000");
});

app.get("/", (req, res) => {
  res.sendFile(path.resolve(__dirname, "index.html"));
});

app.get("/recitar", (req, res) => {
  fs.readFile(
    path.resolve(__dirname, "priv", "poema.txt"),
    "utf8",
    (err, data) => {
      if (err) {
        res.status(500).send("Error reading the file");
      } else {
        res.json({
          text: data.replace(/\n/g, "<br>"),
        });
      }
    }
  );
});
