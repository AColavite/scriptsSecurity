const Ticket = require('../models/ticketModel');

const createTicket = async (req, res) => {
    const { subject, description } = req.body;

    const ticket = await Ticket.creat ({
        subject,
        description,
        user: req.user._id
    });

    res.status(201).json(ticket);
};

const getMyTickets = async (req, res) => {
    const tickets = await Ticket.find({ user: req.user._id });
    res.json(tickets);
};

Module.exports = { createTicket, getMyTickets};