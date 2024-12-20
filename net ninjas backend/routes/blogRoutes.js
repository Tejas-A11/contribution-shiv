const express = require('express');
const blogController = require('../controller/blogController')
const router = express.Router();

// blog routes
router.get('/', blogController.blog_index)

// post request to create blog
router.post('/', blogController.blog_create_post)

router.get('/create', blogController.blog_create_get)

router.get('/:id', blogController.blog_details)

router.delete('/:id', blogController.blog_delete)
// fetch is a AJAX request hence we can not send a redirect as it's response

module.exports = router;