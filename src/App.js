import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Header from './components/Header';
import Home from './components/Home';
import RecipeForm from './components/RecipeForm';
import Database from './components/Database';
import Settings from './components/Settings';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route exact path="/" element={<Home />}/>
        <Route path="/save-recipe" element={<RecipeForm />}/>
        <Route path="/database" element={<Database />}/>
        <Route path="/settings" element={<Settings />}/>
      </Routes>
    </Router>
  );
}

export default App;
