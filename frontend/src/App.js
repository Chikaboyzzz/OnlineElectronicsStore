import React from 'react';
import './App.css';
import ProductList from './components/ProductList';

import Header from './Header';

function App() {
  return (
  <div>
  <Header />
    <div className="container">
      <ProductList />
    </div>
    </div>
  );
}

export default App;