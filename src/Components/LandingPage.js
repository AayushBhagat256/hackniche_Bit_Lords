import React from 'react'
import BrandExample from './NavLand'
import Typewriter from 'typewriter-effect'
// import React from 'react'
import Carousel from 'react-bootstrap/Carousel';
import salute from './salute.jpg'
import './App.css'

function LandingPage() {
    return (
        <div>
            <BrandExample />
            {/* <Carousel/> */}
            <div className="caurosel">
                <Carousel>
                    <Carousel.Item>
                        <a href="/" >
                            <img
                                className="d-block w-100"
                                height={550}
                                src={salute}
                                alt="First slide"
                            />
                        </a>

                        <Carousel.Caption style={{ textDecoration: 'none', color: 'black' }}>
                            <h3><a href="https://weatherapp-256.netlify.app/" style={{ color: 'black' }}>Weather App</a></h3>
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img
                            height={550}
                            className="d-block w-100"
                            src={salute}
                            alt="Second slide"
                        />

                        <Carousel.Caption>
                            <h3 className='pro2'>Recipe Pool</h3>
                            {/* <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p> */}
                        </Carousel.Caption>
                    </Carousel.Item>
                    <Carousel.Item>
                        <img
                            className="d-block w-100"
                            height={550}
                            src={salute}
                            alt="Third slide"
                        />

                        <Carousel.Caption>
                            <h3>Quiz App</h3>
                            {/* <p>
            Praesent commodo cursus magna, vel scelerisque nisl consectetur.
          </p> */}
                        </Carousel.Caption>
                    </Carousel.Item>
                </Carousel>
            </div>

            <div className="content">
                <div className="typingquotes">
                    <Typewriter
                        options={{
                            loop: true,
                            autoStart: true,
                            delay: 50,
                            strings: [
                                "For the veteran, thank you for bravely doing what you’re called to do so we can safely do what we’re free to do.",
                                "They are not just soldiers they are our heroes",
                                "A hero is someone who has given his or her life to something bigger than oneself."
                            ]
                        }}
                    />
                </div>
                <br />
                <div className="buttons">
                    {/* <h1>hi here will be login button</h1> */}
                    <div class="box-1">
                        <div class="btnn btn-one">
                            <span>Log-In</span>
                        </div>
                    </div>
                    {/* Register  */}
                    <div class="box-1">
                        <div class="btnn btn-one">
                            <span>Register</span>
                        </div>
                    </div>
                </div>
            </div>
            
        </div>
    )
}

export default LandingPage