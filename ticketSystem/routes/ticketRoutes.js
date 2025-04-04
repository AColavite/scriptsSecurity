const express = require('express');
const router = express.Router();
const { createTicket, getMyTickets } = require('../controllers/ticketController');
const protect = require('../middlewares/auth');

router.post('/', protect, createTicket);
router.get('/', protect, getMyTickets);

module.exports = router;
