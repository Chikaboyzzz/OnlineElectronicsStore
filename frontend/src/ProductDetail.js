import React, { useState, useEffect } from "react";

function ProductDetail(props) {
  const [product, setProduct] = useState({});
  const productId = props.id;

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/v1/product/${productId}/`)
      .then((res) => res.json())
      .then((data) => setProduct(data));
  }, [productId]);

  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <p>{product.price}</p>
    </div>
  );
}

export default ProductDetail;
