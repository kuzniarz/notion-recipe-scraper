import Container from 'react-bootstrap/Container';
import Card from 'react-bootstrap/Card';

function Home() {
    return (
        <Container className="d-flex align-items-center">
            <Container className="d-flex justify-content-center">
                <Card className="w-75">
                <Card.Header><b>Welcome to the Notion-Recipe-Scraper</b></Card.Header>
                <Card.Body>
                    <Card.Text>This application is intended to facilitate the scraping and saving
                    of recipies to a configured Notion Database. To setup the notion database,
                    go to the settings tab and set your Notion database id. Afterwards you
                    can use the 'Save Recipe' menu item to save recipies.
                    </Card.Text>
                </Card.Body>
                </Card>
            </Container>
        </Container>
      );
}

export default Home;