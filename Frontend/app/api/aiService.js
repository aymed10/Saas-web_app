export const fetchGeneratedText = async (prompt) => {
    try {
      const apiUrl = `http://localhost:8000/chatbot`;
      console.log(apiUrl)
      
      const response = await fetch(apiUrl, {
        method: "POST", 
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
        },

        body: JSON.stringify({ message: prompt })
      });
      
      if (!response.ok) {
        throw new Error("Failed to fetch AI response. Status: ${response.status}");
      }
      
      // Return the fetched data 
      return await response.json(); 
    } catch (error) {
      console.error("API Error:", error);
      
      // Allow the component to handle the error
      throw error; 
    }
  };
  