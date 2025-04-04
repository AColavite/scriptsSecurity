import { CodingBlog } from "../models/blog.model.js";

export const getBlogs = async (req, res) => {
    try {
        const blogs = await CodingBlog.find({});
        
        if (blogs.length === 0) {
            return res.status(404).json({ error: "No blogs found" });
        }

        res.status(200).json(blogs);
    } catch (error) {
        console.error("Error in fetching coding blogs:", error);
        res.status(500).json({ error: "Internal Server Error" });
    }
};

export const postBlog = async (req, res) => {
    try {
        const { name, content } = req.body;

        if (!name || !content) {
            return res.status(400).json({ error: "All fields are required" });
        }

        const newBlog = new CodingBlog({
            type: "coding",
            name,
            content
        });

        const savedBlog = await newBlog.save();
        res.status(201).json(savedBlog);
    } catch (error) {
        console.error("Error in posting coding blog:", error);
        res.status(500).json({ error: "Internal Server Error" });
    }
};
