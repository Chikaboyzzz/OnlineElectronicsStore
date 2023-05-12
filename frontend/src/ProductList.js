import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

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
      <h2>Products</h2>
        {products.map(product => (
          <li key={product.id}>
            <h3>
                <a href={`/products/${product.id}`}>{product.name}</a>
            </h3>
          </li>
        ))}
    </div>
  );
}

export default ProductList;
