import React from 'react';
import ProductList from './ProductList';
import ProductDetail from './ProductDetail';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';


function App() {
  return (
    <div>
      <h1>My ReactJS Application</h1>
      <ProductList />
      <Routes>
        <Route path="/products/:productId" element={<ProductDetail />} />
      </Routes>
    </div>
  );
}

export default App;