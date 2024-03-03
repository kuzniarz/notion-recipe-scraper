import './RecipeForm.css'
import React, { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

function RecipeForm(){
    return (
      <Container className="justify-content-md-center">
            <Card className="">
            <Card.Header><b>Settings</b></Card.Header>
            <Card.Body>
                <Form>
                    <Form.Group className="mb-3" controlId="url">
                        <Form.Label><b>Recipe URL</b></Form.Label>
                        <Form.Control type="url" placeholder="eg. https://cooking.nytimes.com/recipes/9530-lasagna" />
                        <Form.Text className="text-muted">
                        Please keep in mind that the recipe-scraper supports a limited set of recipe pages.
                        </Form.Text>
                    </Form.Group>
                    <Container className="justify-content-right">
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                    </Container>
                </Form>
            </Card.Body>
            </Card>
        </Container>
    );
}

function ApiResponse() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(json => setData(json))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="apiResponse">{data ? <pre>{JSON.stringify(data, null, 2)}</pre> : 'Loading...'}</div>
  );
}

export default RecipeForm;