# **Shop K-Beauty Testing Results**

![amiresponsive mock-ups of SHOP K-BEAUTY](./documentation/responsiveness/am-i-responsive.png)
### [Link to the Deployed App](https://shop-k-beauty-django-joy-zadan.herokuapp.com/)
---
## TABLE OF CONTENTS
---
* Automated Testing
    * HTML Validation
    * CSS Validation
    * JavaScript Validation
    * Python Validation
    * Lighthouse Report
        * Desktop
        * Mobile
    * WAVE Web Accessibility Evaluation Tool
    * a11y Color Contrast Accessibility for the Visually Impaired Test Results
    * Responsive Design Testing
    * Django Unit Testing
        * Django Unit Testing - Issues
        * Djangon Unit Testing - Unsolved Issues
* Manual Testing
    * Testing User Stories
    * Full Manual Testing
* Bugs, Errors & Solutions
    * Solved Bugs
    * Unsolved Bugs
---

# Bugs, Errors & Solutions
| # | Bugs, Errors and Issues | Solutions |
| :--- | :--- | :--- |
| 1 | Error: You are trying to add a non-nullable field to without a default  | Solution: Choose option 1 from two options provided by Django when making migrations, add timezone.now, then migrate. New error appeared: ```TypeError: Field 'id' expected a number but got datetime.datetime(2022, 11, 20, 13, 54, 36, 590663, tzinfo=<UTC>)```. I then looked for the latest _auto_ file from migrations folder, then changed ```default=got datetime.datetime(2022, 11, 20, 13, 54, 36, 590663, tzinfo=<UTC>)``` to ```default=1```. I was then able to migrate successfully. |
| 2 | Stripe Webhook errors, ```401 ERR```, x 23 times and 100% failure rate  |  After numerous attempts to solve this by going over and over the source code for webhook handlers, searching the Stripe docs and, stackover and slack, the solution to share my GitPod workspace |
| 3 | Reviews were not deleting after an associated product is deleted  |  Fortunately, this was a simple bug. I just had to edit the product (fk) in my review model. ``` on_delete=models.SET_NULL``` was changed to ``` on_delete=models.CASCADE ```, then migrate. |
| 4 | HTML Validation errors on add a product and edit a product pages in products app : ```Error: Duplicate attribute id. At line 1351 column 69 id="id_image"``` | This is a very interesting error, caused by conflicts between multiple languages. First, the JQuery script to change the image file uses an id of ```#new-image```. This caused a conflict with Django's forms widget clearable_file_input, ````{% include "django/forms/widgets/attrs.html" %}````, which comes with a function ```def clear_checkbox_id(self, name): """Given the name of the clear checkbox input, return the HTML id for it.""" return name + "_id"``` (see from line 438: [Github:Django/Django](https://github.com/django/django/blob/main/django/forms/widgets.py)). Because the script already uses ```#id-image```, when the file input is selected, it returns the HTML id, which resulted in HTML validation error of duplicate atttribute id. | The solutions came in several steps:
1. Change the JQuery script from ``` #new-image``` to ```.new-image```
2. Change the custom_clearble_file_input.html (line 19): from ```<input id="new-image">``` to ```.new-image ```
3. We cannot leave it here because the forms.py file in the products app has a forloop that adds class attributes:
```for field_name, field in self.fields.items(): field.widget.attrs['class'] = 'border-black rounded-0'```. Left unsolved, we would just be exchanging a duplicate id error with a duplicate class error. So I deleted this forloop.
4. To still have the ```border-black rounded-0``` attributes added to the add/edit a product forms, I then added these to new attributes to base.css ```.select, .form-control {border: 1px solid #000 !important; border-radius: 0 !important;}```

| # | Unsolved Bugs, Errors and Issues | Justification |
| :--- | :--- | :--- |
| 1 | Browser: Chrome, Error: **Uncaught (in promise) Error: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received**. This error appears after about a minute or two of loading any page of the web application. | I have spent days looking for where this error was coming from, initially thinking it was caused by the show and hide button on the homepage to hide and show list of available brands. I switched off the event listener. The error still appeared. I tried to debug and refactor all the event listeners but found it impossible to do so without disabling the required JQuery functions for the application to run smoothly. Googling for possible causes and reasons, I have found references to the same error and they point to using incognito mode as a possible solution. The error did not appear when using incognito mode. Due to time constraints, the real solution for this error may be investigated further on the next sprint/ future development. |
