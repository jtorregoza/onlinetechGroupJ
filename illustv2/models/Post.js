const mongoose = require("mongoose");

const PostSchema = new mongoose.Schema({
  user: { type: String, required: true },
  title: { type: String, required: true },
  description: { type: String, required: true },
  rating: { type: String, required: true },
  date: { type: Date, required: true },
  img: { type: String, required: true }
});

module.exports = mongoose.model("Post", PostSchema);
