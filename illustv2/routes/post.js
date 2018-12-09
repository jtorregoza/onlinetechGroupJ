const express = require("express");
const router = express.Router();
const mongoose = require("mongoose");
const Post = require("../models/Post");
const User = require("../models/User");

mongoose.connect("mongodb://localhost/piciv");
let db = mongoose.connection;

db.once("open", () => console.log("Connected"));
db.on("error", err => console.log(err));

router.get("/post/:postId", (req, res) => {
  let postId = req.params.postId;
  Post.findOne({ _id: postId }, (err, result) => {
    if (!err && result) {
      let { user, title, description, rating, date, img } = result;
      res.json({
        user: user,
        title: title,
        description: description,
        rating: rating,
        date: date,
        img: img
      });
    } else {
      res.status(500).send({ message: "Failed to fetch data" });
    }
  });
});

router.post("/post", (req, res) => {
  let { user, title, description, rating, date, img } = req.body;

  let newPost = new Post({
    user: user,
    title: title,
    description: description,
    rating: rating,
    date: date,
    img: img
  });
  newPost.save();
  res.send({ message: "Ok" });
});

module.exports = router;
