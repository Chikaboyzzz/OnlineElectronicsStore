import React from 'react';
import ProductList from './ProductList';
import ProductDetail from './ProductDetail';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';


function App() {
  return (
    <div>
        <Header />
        <ProductList/>
    </div>);
}

export default App;


const Header = function(){
return(<Navbar bg="dark" variant="dark" expand="md">
  <Container>
    <Navbar.Brand href="#home" className="text-light">Navbar with text</Navbar.Brand>
    <Navbar.Toggle />
    <Navbar.Collapse className="justify-content-end">
      <Navbar.Text>
        Signed in as: <a href="#login" className="text-light">Username</a>
      </Navbar.Text>
    </Navbar.Collapse>
  </Container>
</Navbar>

    )
}

