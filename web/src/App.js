import React, { useState } from 'react';

function App() {
  const [texte, setTexte] = useState('');
  const [message, setMessage] = useState('');

  const verifierTexte = async () => {
    const response = await fetch('http://localhost:5000/verifier-texte', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ texte }),
    });

    const data = await response.json();

    setMessage(data.message);
  };

  return (
    <div>
      <textarea
        value={texte}
        onChange={(e) => setTexte(e.target.value)}
        placeholder="Entrez du texte ici"
      />
      <button onClick={verifierTexte}>Vérifier</button>
      <p>{message}</p>
    </div>
  );
}

export default App;
