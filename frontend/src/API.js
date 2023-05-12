import axios from 'axios';
import './App.css';
import AddMovie from './AddMovie'

export default axios.create({
    baseURL: "http://127.0.0.1:8000/backend_api/movies",
    headers: {
        'Accept':'application/json',
        'Content-Type':'application/json',
    }
})



