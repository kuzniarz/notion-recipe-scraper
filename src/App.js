import './App.css';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Header from './components/Header/Header';
import Home from './pages/Home';
import RecipeForm from './pages/RecipeForm';
import Database from './pages/Database';
import Settings from './pages/Settings';

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
