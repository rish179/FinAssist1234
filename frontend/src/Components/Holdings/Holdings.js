import React, { useState } from "react";
import './Holdings.css'

function Holdings({user_credentials,UpdateNewsData,Isfetching}) {

    const [holdings_data,set_holdings_data] = useState([])

    async function fetchData_backend(endpoint, body) {
        // Sending HTTP Request to fetch data 
        try {
        const response = await fetch(`http://127.0.0.1:5000//backend/${endpoint}`, {
            method: 'POST', // POST Request
            headers: {},
            body: body,
            });

        // If Response is received
        if (!response.ok) {// If Response status code is not 200 ( not success ) 
            throw new Error(`HTTP error! Status: ${response.status}`); // Threw Error
        }

        return await response.json(); // Return response in json format if status code is 200 
        }
        catch (error) {
            console.error('Fetch error:', error);
        throw error;
        }
    };

            
    const UploadCSVFile_thresholds = async (csvFile) => {
        if (!csvFile) {
            alert('Please select a file to upload.');
            return;
        }

        const formData = new FormData();
        formData.append('file', csvFile);

        Isfetching(true)

        try {
            const dataResponse = await fetchData_backend('upload_csv', formData);
            set_holdings_data(JSON.parse(dataResponse['Holdings']))

            UpdateNewsData(dataResponse['RelatedArticles'])

            Isfetching(false)


        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

    const handle_Threshold_FileChange = (e) => {
        const selectedFile = e.target.files[0];
        if (selectedFile && selectedFile.type === 'text/csv') {
            UploadCSVFile_thresholds(selectedFile);
            e.target.value = null; // Reset the input value
        } else {
            alert('Please upload a valid CSV file.');
        }
    };

    return (
        <div className = "Holdings-div">
            <div className = "Holdings-title-div">
                <p className = "Holdings-label">Holdings</p>
                <div className='Holdings-button '>
                    <input 
                        type="file" 
                        accept=".csv" 
                        onChange={handle_Threshold_FileChange} 
                        className='upload_input'
                        id="file-input"/>
                    <label htmlFor="file-input" className="upload_input-label">
                        Upload csv
                    </label>
                </div>
            </div>
            <div className="Holdings-content-div">
                {holdings_data.map(item => 
                    <div className = "Holdings-content">
                        <p className = "Holdings-name">{item.Stocks}</p>
                        <div className = "Holdings-info-div">
                            <p className = "Holding-label">QTY :</p>
                            <p className = "Holding-value">{item.Quantity}</p>
                            <p className = "Holding-label price_label">AVG PRICE :</p>
                            <p className = "Holding-value">{item['Avg Price']}</p>
                        </div>
                    </div>
                )}
            </div>
        </div>
    )
};

export default Holdings;