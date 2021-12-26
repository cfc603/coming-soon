# coming-soon
A django project using the [startbootstrap-coming-soon](https://github.com/StartBootstrap/startbootstrap-coming-soon) theme

## Preview

[![Coming Soon Preview](preview.png)](https://coming-soon.trevorwatson.info/)

**[View Live Preview](https://coming-soon.trevorwatson.info/)**

## Deploy to PythonAnywhere

### Sign Up!

If you have not already created an account on [PythonAnywhere][1], visit there site at https://www.pythonanywhere.com/ and select ***Pricing & signup***. You can use any of the account options, however, the free **Beginner** account will not allow you to use your own domain.

### Setup your first webapp

While [PythonAnywhere][1] has a great user interface to setup new web applications, the quickest route is via their CLI. Let's set that up:

- Generate a new API token by selecting ***Account*** then ***API Token*** and finally ***Create new token***
- Open up a **Bash** console by selecting ***Dashboard*** then ***$ Bash*** under **New console:**. Run the following in your new **Bash** console:
```bash
pip install --user pythonanywhere
```

Depending on whether or not your using your own domain, or the one provided by [PythonAnywhere][1], the next step will vary slightly

#### With your domain:

```bash
pa django autoconfigure https://github.com/cfc603/coming-soon -p 3.9 -d www.yourdomain.com
```

Next you will need to point your domain to your [PythonAnywhere][1], if you need assistance with this, checkout these [instructions](https://help.pythonanywhere.com/pages/CustomDomains#configuring-the-domain-at-the-domain-registrar).

#### [PythonAnywhere][1] domain:

```bash
pa django autoconfigure https://github.com/cfc603/coming-soon -p 3.9
```

### Going Live

At this point your site should be up and running, but there are a few more steps you will want to take to ensure your site is secure. [Django][2] offers many builtin security features, most of which are enabled, but there are a few that need to be enabled on deployment. You can find a checklist at https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/ which goes over the features in detail, or if you are in a hurry you can run the following command in your open terminal:

```bash
python manage.py check --deploy
```
The output should look like the following:

```bash
System check identified some issues:

WARNINGS:
?: (security.W004) You have not set a value for the SECURE_HSTS_SECONDS setting. If your entire site is served only over SSL, you may want to consider setting a value and enabling HTTP Strict Transport Security. Be sure to read the documentation first; enabling HSTS carelessly can cause serious, irreversible problems.
?: (security.W008) Your SECURE_SSL_REDIRECT setting is not set to True. Unless your site should be available over both SSL and non-SSL connections, you may want to either set this setting True or configure a load balancer or reverse-proxy server to redirect all connections to HTTPS.
?: (security.W009) Your SECRET_KEY has less than 50 characters, less than 5 unique characters, or it's prefixed with 'django-insecure-' indicating that it was generated automatically by Django. Please generate a long and random SECRET_KEY, otherwise many of Django's security-critical features will be vulnerable to attack.
?: (security.W012) SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
?: (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True. Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.
?: (security.W018) You should not have DEBUG set to True in deployment.

System check identified 6 issues (0 silenced).
```

All these options need to be set in your settings file which can be accessed in the file navigator. Open a new tab to the [PythonAnywhere][1] home screen as we will still need the console open for the next step. Select ***Files*** from the navigation menu. The Files menu is setup with the directories on the left side and files within the current directory on the right. Under directories you should see something similar to:

- .cache/
- .local/
- .ssh/
- .virtualenv/
- .your-username.pythonanywhere.com/

Or if you used your own domain:

- www.yourdomain.com/

Within this directory are all the project files for your website. Select the appropriate directory and you should see a new list of directories, select `coming_soon/`, and finally on the right side, select `settings.py`. Looking back at the terminal, we have the following settings that should be reviewed and updated:

```
SECURE_HSTS_SECONDS
SECURE_SSL_REDIRECT
SECRET_KEY
SESSION_COOKIE_SECURE
CSRF_COOKIE_SECURE
DEBUG
```

Two of which are listed in the first few lines, `DEBUG` and `SECRET_KEY`. [Django][2] generates a temporary `SECRET_KEY` when you start the project but should be changed on deployment, more details can be found here https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key. To generate a new one, run the following command in the terminal:

```bash
python manage.py shell -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Copy the output and update `SECRET_KEY` in `settings.py`. Right below is the `DEBUG` setting which is set to `True`, where the `python manage.py check --deploy` command states it should be `False` when deployed, update this as well. Now click the *Save* button in the top right hand corner. And go back to the terminal and run `python manage.py check --deploy` again.

#### SSL

The remaining settings are dependent on your site having a **HTTPS** certificate. If your using the [PythonAnywhere][1] supplied URL, this is automatically enabled. Using your own domain, we will need to enable it. You may want to open another tab to [PythonAnywhere][1] as we will still need the console and `settings.py`.

Once open, select ***Web*** from the navigation menu, next, select the domain name on the left side, if it is not already selected. Scroll down towards the bottom of the page until you see **Security** and select the ***pencil*** icon to the right of **HTTPS certificate**. Choose ***Auto-renewed Let's Encrypt certificate*** and select **Save**. Also enable ***Force HTTPS***. While the directions state to, "You need to Reload your web app to activate any changes made below," we will be doing this after changing the other settings.

Going back to the `settings.py`, enter the following and select ***Save***:

```python

# SSL
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

```

You may have noticed `SECURE_HSTS_SECONDS` is missing. As the `python manage.py check --deploy` command states, "Be sure to read the documentation first; enabling HSTS carelessly can cause serious, irreversible problems", I'll leave a link to the documentation and give an additional caution on enabling it: https://docs.djangoproject.com/en/4.0/ref/middleware/#http-strict-transport-security

Go back to our console to ensure everything was entered properly and run the command again `python manage.py check --deploy`. If everything looks as expected, go back over to your open **Web** tab and at the very top select ***Reload***. This reloads your ``settings.py`` and enables all other changes to your website.

### Retrieving Form Submissions

As people signup, you will need to be able to access the email addresses entered. [Django][2] has a built in admin console which can be found by adding `/admin/` to the end of your website domain. You will be prompted for a username and password which can be created by going back to the console and entering `python manage.py createsuperuser`. Once complete go back to the login page and you should be able to login. The emails can be found under the **Registration** menu and selecting ***Entrys***.

### Success

Congratulations on deploying the **coming-soon** project. If you have any questions, feel free to reach out via my [Contact Form](https://www.trevorwatson.info/contact/contact-entry/create/)

[1]: https://www.pythonanywhere.com/
[2]: https://www.djangoproject.com/
