
import { useEffect, useState } from 'react';
import './NewsContainer.css'

function NewsContainer({newsDate}) {

    const [newsData_cl,set_newsData_cl] = useState([])


    useEffect(() => {
        
        if (Object.keys(newsDate).length > 0) {
            let newsData_temp = []
    
            newsDate.forEach(element => {
                if (Array.isArray(element[1]) && element[1].length > 0) {
                    newsData_temp.push(...element[1]); // ✅ spread into the array
                }
            });
        
            set_newsData_cl(newsData_temp)
        }

    },[newsDate])

    return (
        <div className = "NewsContainer-div" hre>
            <p className = "NewsContainer-label">Related News</p>
            <div className = "NewsContainer" >
                {newsData_cl.map((item,index) => 
                    <div className = "NewsContainer-item" key={index} onClick={() => window.open(item.url, '_blank')}>
                        <p className = 'NewsContainer-item-label'>{item.headline}</p>
                    </div>
                )}
            </div>
        </div>
    )

};

export default NewsContainer;