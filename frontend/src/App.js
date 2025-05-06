import logo from './logo.svg';
import './static/App.css';
import {useEffect, useState} from 'react';

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(()=>{
    fetch('http://127.0.0.1:8000/api/posts/')
      .then(response => response.json()) //Converte a resposta para JSON
      .then(data => {console.log('dados recebidos',data);
        setPosts(data)})// Atualiza o estado com os dados
      .catch(erro => console.error(`Erro ao buscar os post: ${erro}`));
  },[])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer">
            Learn React
        </a>
        <ul>
        {posts.map(post=>(
          <li key={post.id}>
            <h1>{post.id}</h1>
            <h2>{post.titulo}</h2>
          </li>
        ))}
        </ul>
      </header>
    </div>
  );
}

export default App;
