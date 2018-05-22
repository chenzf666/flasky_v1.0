# Flask-Blogging
前段代码和RESTFUL编程仍未使用服务层的类来编程

Content:
<pre>
flasky_v1.0
│  config.py
│  manage.py
│  requirements.txt
│  wsgi.py
│
├─app
│  │  decorators.py
│  │  email.py
│  │  __init__.py
│  │
│  ├─api
│  │  │  __init__.py
│  │  │
│  │  ├─common
│  │  │      util.py
│  │  │      __init__.py
│  │  │
│  │  └─resources
│  │         comment.py
│  │         post.py
│  │         user.py
│  │         __init__.py
│  │
│  ├─auth
│  │      forms.py
│  │      views.py
│  │      __init__.py
│  │
│  ├─main
│  │      errors.py
│  │      forms.py
│  │      views.py
│  │      __init__.py
│  │
│  ├─models
│  │      anonymousUser.py
│  │      anonymousUser_model.py
│  │      comment.py
│  │      comment_model.py
│  │      follow.py
│  │      follow_model.py
│  │      permission.py
│  │      permission_model.py
│  │      post.py
│  │      post_model.py
│  │      role.py
│  │      role_model.py
│  │      user.py
│  │      user_model.py
│  │
│  ├─repositorys
│  │      base_repository.py
│  │      comment_repository.py
│  │      post_repository.py
│  │      user_repository.py
│  │      __init__.py
│  │
│  ├─services
│  │      comment_service.py
│  │      post_service.py
│  │      user_service.py
│  │      __init__.py
│  │
│  ├─static
│  └─templates
│      │  403.html
│      │  404.html
│      │  500.html
│      │  base.html
│      │  edit_post.html
│      │  edit_profile.html
│      │  followed_by.html
│      │  followers.html
│      │  hello.html
│      │  index.html
│      │  moderate.html
│      │  post.html
│      │  user.html
│      │  _comments.html
│      │  _macros.html
│      │  _posts.html
│      │
│      └─auth
│          │  login.html
│          │  register.html
│          │  unconfirmed.html
│          │
│          └─email
│                  confirm.html
│                  confirm.txt
│
├─migrations
├─tests
│      tests_basics.py
│      test_user_model.py
│      __init__.py
│
└─venv
</pre>
