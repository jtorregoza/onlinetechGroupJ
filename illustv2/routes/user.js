const express = require("express");
const router = express.Router();
const mongoose = require("mongoose");
const User = require("../models/User");

mongoose.connect("mongodb://localhost/piciv");
let db = mongoose.connection;

db.once("open", () => console.log("Connected"));
db.on("error", err => console.log(err));

router.get("/user/:username", (req, res) => {
  let username = req.params.username;
  User.findOne({ username: username }, (err, result) => {
    if (!err && result) {
      res.json({
        id: result.id,
        name: result.name,
        username: result.username,
        email: result.email,
        bio: result.bio,
        posts: result.posts
      });
    } else {
      res.status(500).send({ message: "Failed to fetch data" });
    }
  });
});

router.post("/user", (req, res) => {
  let { username, password, email, name, bio } = req.body;

  let newUser = new User({
    name: name,
    username: username,
    password: password,
    bio: bio,
    email: email,
    posts: []
  });
  newUser.save();
  res.send({ message: "Ok" });
});

module.exports = router;
