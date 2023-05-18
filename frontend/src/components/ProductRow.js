import sampleImage from '../logo192.png';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductRow = () => {
  const [products, setProducts] = useState([]);
  const [productDetails, setOtherData] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/v1/product/')
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/v1/productDetail/')
      .then(response => {
        setOtherData(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div className="row product">
      <div className="col-md-2">
        {products.map(product => (
          <div key={product.id}>
            <img src={`http://127.0.0.1:8000/api/v1/product/image/${product.id}`} alt="Product" height="150" />
          </div>
        ))}
      </div>
      <div className="col-md-8 product-detail">
        {products.map(product => (
          <h4 key={product.id}>
            {product.name}
          </h4>
        ))}
        {productDetails.map(productDetail => (
          <div key={productDetail.id}>
            {productDetail.description}
          </div>
        ))}
      </div>
      <div className="col-md-2 product-price">
        {productDetails.map(productDetail => (
          <div key={productDetail.id}>
            {productDetail.price}
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProductRow;

//const ProductRow2 = () => {
//  const [products, setProducts] = useState([]);
//
//  useEffect(() => {
//    axios.get('http://127.0.0.1:8000/api/v1/productDetail/')
//      .then(response => {
//        setProducts(response.data);
//      })
//      .catch(error => {
//        console.log(error);
//      });
//  }, []);
//  return (
//    <div className="row product">
//      <div className="col-md-2">
//        <img src={sampleImage} alt="Sample Image" height="150" />
//      </div>
//      <div className="col-md-8 product-detail">
//        {products.map(product => (
//        <li key={product.id}>
//            {product.name}
//        </li>
//      ))}
//      </div>
//      <div className="col-md-2 product-price">
//        $19.99
//      </div>
//    </div>
//  );
//}

//import {  BrowserRouter as Router,  Routes,  Route, Link} from "react-router-dom";
//
//function ProductList() {
//  const [products, setProducts] = useState([]);
//
//  useEffect(() => {
//    axios.get('http://127.0.0.1:8000/api/v1/product/')
//      .then(response => {
//        setProducts(response.data);
//      })
//      .catch(error => {
//        console.log(error);
//      });
//  }, []);
//
//  return (
//    <div>
//      {products.map(product => (
//        <li key={product.id}>
//          <h3>
//            {product.name}
//          </h3>
//        </li>
//      ))}
//    </div>
//
//  );
//}
//
//
//export default ProductList;
