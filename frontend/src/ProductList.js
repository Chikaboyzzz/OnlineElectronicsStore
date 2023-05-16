import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {  BrowserRouter as Router,  Routes,  Route, Link} from "react-router-dom";

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/v1/product/')
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Product List</h1>
      {products.map(product => (
        <li key={product.id}>
          <h3>
            {product.name}
          </h3>
        </li>
      ))}
    </div>

  );
}


export default ProductList;
