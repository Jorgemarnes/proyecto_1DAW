# Investigation
In order to populate our music web-store with high-quality and realistic data, we have researched several sources to obtain albums, artists, and pricing information.

---

## Search Evidence & Documentation
We analyzed the following options found through GitHub repositories and developer portals: 

<br>

### Option 1: Spotify Web API
**Type:** REST API  
**Link:** https://developer.spotify.com/documentation/web-api  
**Rsearch Notes:** The industry standard for music data, including popularity metrics and audio features.  
**Advantages:** Extremely rich data and integrates well with modern music trends.  
**Disadvantages:** Requires a premium Spotify account, complex authentication process and an active developer account.  

<br>

### Option 2: MusicBrainz
**Type:** Open Database  
**Link:** https://musicbrainz.org/  
**Research Notes:** An open-source project with a massive community-driven encyclopedia of music.  
**Advantages:** Completely free and open-source with no commercial restrictions.  
**Disadvantages:** The data structure is very complex and can be difficult for a first-time web project.

<br>

### Option 3: iTunes Search API
**Type:** Public API  
**Link:** https://performance-partners.apple.com/search-api  
**Research Notes:** A straight forward API that provides metadata and high-quality album artwork.  
**Advantages:** No authentication required, no API key needed, very fast response times, and provides direct links to album covers.  
**Disadvantages:** Less metadata compared to specializaed music databases.  

<br>

### Option 4: Rough Trade
**Type:** Web  
**Link:** https://www.roughtrade.com  
**Research Notes:** Excellent for physical product layout, vinyl pricing, and descriptions.  
**Advantages:** Real-world vinyl pricing, expert album reviews, and high-quality bountique curation.  
**Disadvantages:** No API available (requires manual copy), data is static, and hard to scale.  

<br>

## Final Choice: iTunes API
We chose iTunes Search API. It is the most efficient way to get high-quality images and real music data automatically without the need for manual data entry or complex authentication.