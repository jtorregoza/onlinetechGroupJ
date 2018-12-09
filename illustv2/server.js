const express = require("express");
const bodyParser = require("body-parser");
const UserRoute = require("./routes/user");
const PostRoute = require("./routes/post");

const PORT = 5000;

// Express config
const app = express();
app.use(bodyParser({ extended: false }));

// Routes
app.get("/", (req, res) => {
  res.send("OK");
});

app.use("/api", UserRoute);
app.use("/api", PostRoute);

app.listen(PORT, () => console.log(`Serving at PORT: ${PORT}`));
