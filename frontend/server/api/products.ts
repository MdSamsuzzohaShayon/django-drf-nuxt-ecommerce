export default defineEventHandler(async (event)=>{
    console.log('New request: ' + getRequestURL(event));
    const query = getQuery(event)
    const body = await readBody(event)
    return {
        message: `Hello | ${query?.name} | ${body.age}`
    }
}) ;