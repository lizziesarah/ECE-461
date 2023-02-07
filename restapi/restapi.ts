async function FetchNPMRepo() {
    const endpoint = "https://registry.npmjs.org/package";
    const res = await fetch(endpoint);
    const data = await res.json();
    console.log(data['license']);
}

FetchNPMRepo()