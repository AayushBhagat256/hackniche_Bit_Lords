import Signin from './Components/Signin';
import Signup from './Components/Signup';
import {
  BrowserRouter as Router,
  Route,
  Link,
  Routes,

} from "react-router-dom";
import LandingPage from './Components/LandingPage';



function App() {
  return (
    // <Routes>
    // <Route path='/' element={<Signin/>}/>
    // <Route path='/Signin' element={<Signin/>}/>
    // <Route path='/Signup' element={<Signup/>}/>
    // </Routes>
    <LandingPage/>
  );
}

export default App;
