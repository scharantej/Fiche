## Design for Internal Re-Use Website

### HTML Files
- **index.html**
    - Home page of the website.
    - Lists all available examples with their titles and descriptions.
- **example.html**
    - A template for displaying individual examples.
    - Includes title, description, and any additional content for the example.

### Routes

**@app.route('/')**
- **GET**: Renders the `index.html` page, displaying the list of examples.

**@app.route('/example/<int:example_id>')**
- **GET**: Renders the `example.html` page, displaying the details of the example with the specified `example_id`.

**Additional Considerations:**
- The application could utilize a database to store and fetch the examples.
- Authentication and authorization can be implemented to ensure only authorized users can access the website.
- Pagination can be added to the home page to allow users to browse through a large number of examples.