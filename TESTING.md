# **Shop K-Beauty Testing Results**

![amiresponsive mock-ups of SHOP K-BEAUTY](./documentation/responsiveness/am-i-responsive-new.png)
**[Link to the Deployed App](https://shop-k-beauty-django-joy-zadan.herokuapp.com/)**
---
## TABLE OF CONTENTS

* [Automated Testing](#automated-testing)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JavaScript Validation](#javascript-validation)
    * [Python Validation](#python-validation)
    * [Lighthouse Report](#lighthouse-report)
        * [Desktop](#desktop)
        * [Mobile](#mobile)
    * [WAVE Web Accessibility Evaluation Tool](#wave-web-accessibility-evaluation-tool)
    * [a11y Color Contrast Accessibility for the Visually Impaired Test Results](#a11y-color-contrast-accessibility-for-the-visually-impaired-test-results)
    * [Responsive Design Testing](#responsive-design-testing)
    * [Django Unit Testing](#django-unit-testing)
        * Django Unit Testing - Issues()
        * Djangon Unit Testing - Unsolved Issues
* [Manual Testing](#manual-testing)
    * [Testing User Stories](#testing-user-stories)
    * [Full Manual Testing](#full-manual-testing)
* [Bugs, Errors & Solutions](#bugs-errors--solutions)
    * [Solved Bugs](#solved-bugs)
    * [Unsolved Bugs](#unsolved-bugs)
---

## Automated Testing
### HTML Validation using [W3C Markup Validation Service](https://validator.w3.org/):
* [Homepage](./documentation/html_validation/homepage-html-validation.png)
* [Products Page](./documentation/html_validation/products-page-html-validation.png)
* [Products Page - New Validation After Modal was Added](./documentation/html_validation/products-page-html-validation-new.png)
* [Add a Product Page](./documentation/html_validation/add-product-html-validation-no-error.png)
* [Edit a Product Page](./documentation/html_validation/edit-product-html-validation-no-error.png)
* [Product Detail Page](./documentation/html_validation/product-detail-page-html-validation.png)
* [Product Detail Page - New Validation After Modal was Added](./documentation/html_validation/product-detail-page-html-validation-new.png)
* [Brand Detail Page](./documentation/html_validation/brand-detail-page-html-validation.png)
* [Add a Review Page](./documentation/html_validation/add-a-review-page-html-validation.png)
* [Edit a Review Page](./documentation/html_validation/edit-a-review-page-html-validation.png)
* [Review Detail Page](./documentation/html_validation/review-detail-page-html-validation.png)
* [Reviews Page](./documentation/html_validation/reviews-page-html-validation.png)
* [Bag Page](./documentation/html_validation/bag-page-html-validation.png)
* [Checkout Page](./documentation/html_validation/checkout-page-html-validation.png)
* [Checkout Success Page](./documentation/html_validation/checkout-success-page-html-validation.png)
* [Sign In Page](./documentation/html_validation/sign-in-html-validation.png)
* [Sign Up Page](./documentation/html_validation/sign-up-html-validation.png)
* [Profile Page](./documentation/html_validation/profile-page-html-validation.png)
* [Privacy Policy Page](./documentation/html_validation/privacy-policy-page-html-validation.png)
* [Terms & Conditiions Page](./documentation/html_validation/terms-and-conditions-page-html-validation.png)
* [Return & Refund Policy Page](./documentation/html_validation/return-refund-policy-page-html-validation.png)
* [Shipping Policy Page](./documentation/html_validation/shipping-policy-page-html-validation.png)

### CSS Validation using [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* [checkout.css](./documentation/css_validation/checkout-css.png)
* [profile.css](./documentation/css_validation/profile-css.png)
* [reviews.css](./documentation/css_validation/reviews-css.png)
* [base.css](./documentation/css_validation/base-css.png)

### JavaScript Validation using [JSHint](https://jshint.com/)
| Page | Result | Test Details & Screenshots |
| ---- | :-: | -------------------------- |
| bag/templates/bag/includes/scroll_to_top_script.html | 0 errors, 0 warnings | [scrollToTop script](./documentation/javascript_validation/scroll-to-top-script.png) |
| bag/templates/bag/includes/quantity_update_remove_script.html | 0 errors, 0 warnings | [updateQuantity and removeItem and reload script](./documentation/javascript_validation/update-quantity-remove-item-reload-script.png) |
| home/templates/home/includes/show_hide_brands_list_script.html | 0 errors, 0 warnings | [show and hide list of brands on click script](./documentation/javascript_validation/show-hide-brands-list-script.png) |
| home/templates/home/includes/pass_data_from_backend_to_js_script.html | 0 errors, 0 warnings| [safely passing data from backend to JavaScript script](./documentation/javascript_validation/safely-passing-data-from-backend-to-javascript-script.png) |
| home/templates/home/includes/pass_data_from_backend_to_js_script.html | 0 errors, 0 warnings | [JQuery for the sort selector box](./documentation/javascript_validation/jquery-for-sort-selector-box-script.png) |
| products/templates/products/includes/quantity_input_script.html | 0 errors, 7 warnings | [Quantity Input Script](./documentation/javascript_validation/quantity-input-script.png) |
| profiles/static/profiles/js/countryfield.js | 0 errors, 0 warnings | [countryfield script](./documentation/javascript_validation/countryfield-script.png) |
| products/templates/products/includes/new_image_widget_script.html | 0 errors, 0 warnings | [new image widget script](./documentation/javascript_validation/new-image-widget-script.png) |


### Python Validation

### [Chrome DevTools' Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to test the performance, accessibility, best practices and SEO of the site
**Desktop**
| Page | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%) | If score is below 90% |
| :-- | :-: | :-: | :-: | :-: | :-- |
| ['templates/home/index.html'](./documentation/lighthouse_report/desktop-index-page-after-image-aspect-ratio-refactor.png) | 98 | 97 | 100 | 100 | Scores are above 90% on average |
| ['templates/products/products.html'](./documentation/lighthouse_report/desktop-products-templates-products-page.png) - Before multi-testing for possible solutions | 57 | 97 | 100 | 100 | Extensive efforts were done to improve the Performance score for desktop by converting all images from png to next-gen webp and moving the Google font link from base.html to base.css. Shop K-Beauty currently has 100 products being rendered on this page. The [opportunities](./documentation/lighthouse_report/desktop-products-templates-products-page-opportunities.png) suggested by Lighthouse to potentially improve the score point to **reduce initial server response time** and **serve static assets with an efficient cache policy** all point to 3rd party services and libraries. As a student project, I am only using Heroku's free dynos with ElephantSQL's free Postgres database and Amazon's free tier S3 to host the media and static files. Reading up on [how to improve the performance of the application](https://help.heroku.com/VKCGHPPB/how-do-i-improve-the-performance-of-my-app), Heroku suggests using production-suitable Dynos and Postgres DB, but these are not free. Meanwhile, Amazon S3's cache control is not working, despite using the same source code from the Boutique Ado walkthrough. Further development time is required to investigate Amazon's [File Cache and/or Amazon CloudFront](https://aws.amazon.com/caching/aws-caching/). Meanwhile, when I validated the [same product page but filtered to show only all specials]((./documentation/lighthouse_report/desktop-products-templates-products-page-all-special-offers.png)), the results improved from Performance: 57% to **Performance: 80%**!.  |
| ['templates/products/products.html'](./documentation/lighthouse_report/desktop-index-page-after-image-aspect-ratio-refactor.png) - After successful code refactor of image aspect ratio | 91 | 97 | 100 | 100 | Never one to give when facing a challenge is a good attitute to having in software development! After a good sleep and testing numerous ways to raise the Performance score (desktop) of the site, the solution that worked and gained significant improvement on the score is to cut in half the image width and size, ie, from original 250px by 300px (aspect ratio of 5:6), I reduced both width and height to 125px by 150px. This not only reduced the time to load the Largest Contentful Paint, the product card fits into smaller screens better. |
| ['templates/products/product_detail.html'](./documentation/lighthouse_report/desktop-product-detail-page.png) | 95 | 98 | 100 | 100 | Scores are above 90% on average |
| ['templates/bag/bag.html'](./documentation/lighthouse_report/desktop-bag-page.png) | 95 | 98 | 100 | 100 | Scores are above 90% on average |
| ['templates/checkout/checkout.html'](./documentation/lighthouse_report/desktop-checkout-page.png) | 88 | 94 | 100 | 100 | Aside from the [opportunities identified by Lighthouse to optimise the checkout page performance](./documentation/lighthouse_report/desktop-checkout-page-opportunities-diagnostics.png), the desktop score may be futher improved by adding an explicit width and height for the image elements. After numerous testing on how best to achieve this, I deemed it best left for now as numerous attempts to fix this resulted in distorted display of an image as it seems to conflict with Bootstrap4's ```w-100``` attribute, unless I add width and height sizing for every single possible media query. This should be looked into though in the next sprint. |
| ['templates/checkout/checkout_success.html'](./documentation/lighthouse_report/desktop-checkout-success-page.png) | 94 | 97 | 100 | 100 | Scores are above 90% on average |

**Mobile**
| Page | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%) | If score is below 90% |
| :-- | :-: | :-: | :-: | :-: | :-- |
| ['templates/home/index.html'](./documentation/lighthouse_report/mobile-home-templates-home-index-page.png) | 79  | 93 | 92 | 98 | Extensive efforts were done to improve the Performance score for mobile by converting all images that appear on the index page (incl the largest contentful paint - hero image) from png to webp and setting explicit height and width to them. The opportunities to increase the score suggested by Lighthouse such as [eliminating render-blocking resources](./documentation/lighthouse_report/mobile-home-eliminate-render-blocking-resources.png) and [reduce unused JS](./documentation/lighthouse_report/mobile-home-reduce-unused-js.png) point to 3rd party libraries: Bootstrap, JQuery and Stripe. |
| ['templates/products/products.html'](./documentation/lighthouse_report/mobile-products-page.png) | 49 | 97 | 100 | 99 | Unfortunately, the Performance score improvement gained from the multiple testing and the image resize did not trickle down to mobile version. The [opportunities suggested by Lighthouse](./documentation/lighthouse_report/mobile-products-page-opportunities.png) include **reduce initial server response time**, **use HTTP/2**, **eliminate render blocking resources (stripe (biggest render blocking resource), bootstrap, base.css-amazonaws, fontawesome, jquery and popper**. These are 3rd party libraries and resources and are needed to make the site work. The diagnostics suggested to **serve static assets with an efficient cache policy** and to **avoid an excessive DOM size**. As mentioned earlier, Amazon S3's cache control is not working, despite using the same source code from the Boutique Ado walkthrough. Further development time is required to investigate Amazon's [File Cache and/or Amazon CloudFront](https://aws.amazon.com/caching/aws-caching/). Meanwhile, for the next sprint, reducing the excessive DOM size should be a priority. |
| ['templates/products/product_detail.html'](./documentation/lighthouse_report/mobile-product-detail-page.png) | 76 | 98 | 100 | 97 | Per the [Opportunities and Diagnostics from Lighthouse](./documentation/lighthouse_report/mobile-product-detail-page-opportunities-diagnostics.png), the main cause of the low Performance score are again like the ones discussed above. |
| ['templates/bag/bag.html'](./documentation/lighthouse_report/mobile-bag-page.png) | 80 | 97 | 100 | 94 | Same as above, the Performance score is affected by 3rd party libraries and resources, as evidenced by [this screenshot](./documentation/lighthouse_report/mobile-bag-page-opportunities-diagnostics.png). |
| ['templates/checkout/checkout.html'](./documentation/lighthouse_report/mobile-checkout-page.png) | 75 | 94 | 100 | 97 | Aside from the [opportunities identified by Lighthouse to optimise the checkout page performance](./documentation/lighthouse_report/mobile-checkout-page-opportunities-diagnostics.png), the mobile score may be futher improved by adding an explicit width and height for the image elements. After numerous testing on how best to achieve this, I deemed it best left for now as numerous attempts to fix this resulted in distorted display of an image as it seems to conflict with Bootstrap4's w-100 attribute, unless I add width and height sizing for every single possible media query. This should be looked into though in the next sprint. |
| ['templates/checkout/checkout_success.html'](./documentation/lighthouse_report/mobile-checkout-success-page.png) | 73 | 97 | 100 | 93 | This is a page with no image being rendered, that had plagued me previously in other pages and that had been fixed, as much as possible. But again, the mobile Performance score – as evidenced by the [opportunities and diagnostics](./documentation/lighthouse_report/mobile-checkout-success-page-opportunities-diagnostics.png) –  is affected by 3rd party libraries and resources, which are required for the sitee's applications to work. |


### WAVE Web Accessibility Evaluation Tool

### a11y Color Contrast Accessibility for the Visually Impaired Test Results

### Responsive Design Testing

### Django Unit Testing
#### Django Unit Testing - Issues
#### Djangon Unit Testing - Unsolved Issues

---
## Manual Testing


### Testing User Stories
### Full Manual Testing

---
## Bugs found during testing and development phase

### Solved Bugs
| # | Bugs, Errors and Issues | Solutions |
| :--- | :--- | :--- |
| 1 | Error: You are trying to add a non-nullable field to without a default  | Solution: Choose option 1 from two options provided by Django when making migrations, add timezone.now, then migrate. New error appeared: ```TypeError: Field 'id' expected a number but got datetime.datetime(2022, 11, 20, 13, 54, 36, 590663, tzinfo=<UTC>)```. I then looked for the latest _auto_ file from migrations folder, then changed ```default=got datetime.datetime(2022, 11, 20, 13, 54, 36, 590663, tzinfo=<UTC>)``` to ```default=1```. I was then able to migrate successfully. |
| 2 | Stripe Webhook errors, ```401 ERR```, x 23 times and 100% failure rate  |  After numerous attempts to solve this by going over and over the source code for webhook handlers, searching the Stripe docs and, stackover and slack, the solution was to share my GitPod workspace |
| 3 | Reviews were not deleting after an associated product is deleted  |  Fortunately, this was a simple bug. I just had to edit the product (fk) in my review model. ``` on_delete=models.SET_NULL``` was changed to ``` on_delete=models.CASCADE ```, then migrate. |
| 4 | HTML Validation errors on add a product and edit a product pages in products app : **Error: Duplicate attribute id. At line 1351 column 69 id="id_image"** | This is a very interesting error, caused by conflicts between multiple languages. First, the JQuery script to change the image file uses an id of ```#new-image```. This caused a conflict with Django's forms widget clearable_file_input, ````{% include "django/forms/widgets/attrs.html" %}````, which comes with a function ```def clear_checkbox_id(self, name): """Given the name of the clear checkbox input, return the HTML id for it.""" return name + "_id"``` (see from line 438: [Github:Django/Django](https://github.com/django/django/blob/main/django/forms/widgets.py)). Because the script already uses ```#id-image```, when the file input is selected, it returns the HTML id, which resulted in HTML validation error of duplicate atttribute id. The solutions came in several steps: 1. Change the JQuery script from ``` #new-image``` to ```.new-image``` 2. Change the custom_clearble_file_input.html (line 19): from ```<input id="new-image">``` to ```.new-image ``` 3. We cannot leave it here because the forms.py file in the products app has a forloop that adds class attributes: ```for field_name, field in self.fields.items(): field.widget.attrs['class'] = 'border-black rounded-0'```. Left unsolved, we would just be exchanging a duplicate id error with a duplicate class error. So I deleted this forloop. 4. To still have the ```border-black rounded-0``` attributes added to the add/edit a product forms, I then added these to new attributes to base.css ``` select, .form-control {border: 1px solid #000 !important; border-radius: 0 !important;}``` |
| 5 | HTML Validation errors on bag page: **Error: Duplicate ID** and a warning of The ``` type ``` attribute is unnecessary for JavaScript resources. | This is an error that seems to be fairly left unsolved in other ecommerce projects I've seen on GitHub. The fix seems fairly daunting at first, as it points to ``` item_id ```,  which when searching for this line of code across the project can be found on contexts.py, urls.py, views.py, on webhook_handler.py, on quantity_form.html and on quantity_input_script.html. After initially feeling intimidated about the potential enormity of debugging this error, the solution is actually fairly simple. First, on quantity_form.html, from the remove link (below the form), delete ``` id ``` and move ``` remove_{{ item.item_id }} ``` inside the attribute ``` class ```, thus ``` class="remove_{{ item.item_id }}" ```. Second, on script below the bag.html, replace ``` var itemId ``` with ``` var itemClass ```, then replace the ``` .attr('id') ``` with ``` .attr('class') ``` and lastly, replace ``` var url = `/bag/remove/${itemId}/`; ``` with ``` var url = `/bag/remove/${itemClass}/`; ```. To remove the warnings, I just removed the ``` type="text/javascript" ```. |
| 6 | HTML Validation errors on checkout page: **Error: The value of the ```for``` tag attribute of the ```label``` element must be the ID of a non-hidden form control** | To fix this error, I took the following steps: 1) Deleted the label tag wrapping the two links to (create an account) and (login). 2) I wrapped said links in a ```<p></p>``` to fix alignments for smaller device. 3) I wrapped the non-link text in ```<span></span>``` to be able to add space between the texts. 4) I tested that by deleting the ``` <label></label> ``` tag and the ```for="id-save-info"``` that was in the label, it will not cause stripe webhooks to stop working, that the links will still work and that a newly created account will still be saved and that there was no adverse effect to the functionalities on the checkout page. I also checked that when I tested the orders, the new orders were indeed saved in the database. Additionally, when searching for a potential fix to this error, I came across an article from [CSS tricks](https://css-tricks.com/html-inputs-and-labels-a-love-story/), which says, we should not put interactive elements inside labels such as links. I left the warning of empty heading caused by the loading-spinner.|
| 7 | **Product name field error on Django admin** when re-adding a just deleted product and **lack of defensive programming** | After I accidentally deleted a product (COSRX Aloe Soothing Sun Cream SPF 50+ PA+++ (50ml)), I realised there are two bugs I needed to fix. 1) The first bug: there was a problem with the name field on my Product model being set to ```unique=True``` since when I tried to add the same product I just deleted, the Django admin showed an error that the name already exists (eventhough the product was no longer in the db) and the product I was trying to add did indeed get added. Thus, even though re-adding the same product was successful, I thought it best to amend the Product model because in a real life situation, products will be deleted and should the same products need to be added in the store again, store owners need not be worried about a Django admin error. 2) The second bug: the lack of defensive programming in the project, specifically on the button that allows a superadmin to delete a product. To fix these two bugs, first, I changed the name field on the product model to ```unique=False```, and ```migrate```.  Second, using a modal, I targeted the delete product buttons on the products page and on the product_detail page so that the superadmin will receive a warning prior to confirming the deletion of a product. |
| 8 | **ValueError: invalid literal for int() with base 10: '2.5'** | I came across this bug accidentally when trying to find solutions to the JSHint validation warnings for Quantity Input Script (products/templates/products/includes/quantity_input_script.html). The quantity form in product_detail.html doesn't allow the input of floats (as is expected). But in bag.html it does, so when a user tries to update a product quantity using floats, it triggers this Django error.  The solution: on bag.html, the script to update a product quantity on click ```form.submit()``` needs to be updated to ```form[0].requestSubmit()```. Credit to [Igor Basuga](https://www.linkedin.com/in/igor-basuga-b2a123111/), currently a Junior Developer and a former Full Stack Software Development Tutor at [Code Institute](https://codeinstitute.net/) for the well documented solution [Debugging - a Detective Story and a Learning Experience](./documentation/solved_bugs/debugging-a-detective-story-igor-ci.pdf) to this bug. |
| 9 | Modal in products.html works in development but not in production | After again accidentally deleting a product, this time in production, I realised that the defensive programming to prevent just this situation by using a modal works in development but not in production. Since the same defensive programming is functioning successfully in product detail page, I used [Computed Diff](https://www.diffchecker.com/text-compare/) to check for any difference in the code and noticed that on products.html page, the delete a product button is [split into several lines](./documentation/solved_bugs/delete-product-button-modal-bug.png), compared to the same code and the same button on product_detail.html which is [all in one line](documentation/solved_bugs/delete-product-button-modal-bug-solved.png). Putting all the code for the delete a product button in one line solved the modal bug not working on products page in production. |
| 10 | Heroku Build failure | Testing ... as failure traceback says **Launching...Push failed due to an unrecognized error, and we've been notified.! Please try pushing again.! If the problem persists, see https://help.heroku.com/ and provide Request ID <>. Meanwhile, there's no error showing on the terminal. Pushing again solved the bug. |

### Unsolved Bugs
| # | Unsolved Bugs, Errors and Issues | Justification |
| :--- | :--- | :--- |
| 1 | Browser: Chrome, Error: **Uncaught (in promise) Error: A listener indicated an asynchronous response by returning true, but the message channel closed before a response was received**. This error appears after about a minute or two of loading any page of the web application. | I have spent days looking for where this error was coming from, initially thinking it was caused by the show and hide button on the homepage to hide and show list of available brands. I switched off the event listener. The error still appeared. I tried to debug and refactor all the event listeners but found it impossible to do so without disabling the required JQuery functions for the application to run smoothly. Googling for possible causes and reasons, I have found references to the same error and they point to using incognito mode as a possible solution. The error did not appear when using incognito mode. Due to time constraints, the real solution for this error may be investigated further on the next sprint/ future development. |

