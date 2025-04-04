const User = require('../models/userModel');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

const generateToken = (id) => jwt.sign({ id }, process.env.JWT_SECRET, { expiresIn: '30d' });

const register = async (req, res) => {
  const { name, email, password } = req.body;
  if (await User.findOne({ email })) return res.status(400).json({ msg: 'Usuário já existe' });

  const hash = await bcrypt.hash(password, 10);
  const user = await User.create({ name, email, password: hash });

  res.status(201).json({
    _id: user._id, name: user.name, email: user.email,
    token: generateToken(user._id)
  });
};

const login = async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email });

  if (user && await bcrypt.compare(password, user.password)) {
    res.json({
      _id: user._id, name: user.name, email: user.email,
      token: generateToken(user._id)
    });
  } else {
    res.status(401).json({ msg: 'Credenciais inválidas' });
  }
};

module.exports = { register, login };
