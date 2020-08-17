from polls.views import (
    index, list_posts, posts_form, posts_post, profile_detail, profile_get,
    profile_post, search_profiles)


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/{user_id:\d+}', profile_detail)
    app.router.add_get('/me', profile_get)
    app.router.add_post('/me', profile_post)

    app.router.add_get('/search', search_profiles)

    app.router.add_get('/posts/{user_id:\d+}', list_posts)
    app.router.add_get('/posts', list_posts)
    app.router.add_get('/posts_form', posts_form)
    app.router.add_post('/posts_post', posts_post)

