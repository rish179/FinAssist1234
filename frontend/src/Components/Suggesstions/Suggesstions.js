

import { useEffect, useState } from 'react';
import './Suggesstions.css'

import Lottie from 'react-lottie';
import Analysing from '../../assets/Analysing.json'

function Suggesstions({newsDate,isloading}) {
    const [Suggesstions_Data,set_Suggesstions_Data] = useState([])

    const [Suggesstion_loading,set_Suggesstion_loading] = useState(false)

    async function fetchData_backend(endpoint, body) {
        try {
            const response = await fetch(`http://127.0.0.1:5000/backend/${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept-Encoding': 'gzip'
                },
                body: JSON.stringify(body),
            });
    
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
    
            return await response.json();
        } catch (error) {
            console.error('Fetch error:', error);
            throw error;
        }
    };
    
    const fetch_suggestion = async (newsDate) => {
    
        let results = [];

        set_Suggesstion_loading(true)

        for (const item of newsDate) {
            const ResponseData_temp = await fetchData_backend("Fetch_sentiments", {
                'symbol': item[0],
                'news': item[1]
            });

            console.log(ResponseData_temp)
            results.push(ResponseData_temp);
        }
    
        set_Suggesstions_Data(results);

        set_Suggesstion_loading(false)
    };

    useEffect(() => {


        if (Object.keys(newsDate).length > 0) {
            fetch_suggestion(newsDate)
        }

    },[newsDate])



    return (
        <div className = "Suggesstions-div">
            <p className = "Suggesstions-label">Suggesstions</p>
            {Suggesstion_loading ? 
            <div className = "Suggesstions-loading">
                <Lottie
                    options={{
                        loop: true,
                        autoplay: true,
                        animationData: Analysing,
                        renderer: 'svg'
                        }}
                        height={250}
                        width={250}
                    />
                <p className='Suggesstions-text'>{Suggesstion_loading?"TradeSense Analysing News":"Fetching News"}</p>
            </div>:
            <div className = {`Suggesstions-content ${Suggesstions_Data.length === 0 ? "Empty_content":""}`}>
                {Suggesstions_Data.length === 0 ? 
                <p className='Suggesstions-message'>Upload holdings for AI Suggesstions and News</p>:
                <ul className='Suggesstions_AI-div'>
                    {Suggesstions_Data.map(item => <li className='Suggesstions-items'><span className='suggestion_stock_symb'>{item['Symbol']}</span> : {item['Sentiments']}</li>)}
                </ul>}
            </div>}
        </div>

    )
};

export default Suggesstions;