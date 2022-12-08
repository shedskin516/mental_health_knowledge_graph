from api.exceptions.notfound import NotFoundException

class DiseaseDAO:
    """
    The constructor expects an instance of the Neo4j Driver, which will be
    used to interact with Neo4j.
    """
    def __init__(self, driver):
        self.driver = driver


    # get detail of specific disease by its name
    def getDisease(self, disease_name):

        def get_detail_by_disease(tx, disease_name):
            result = tx.run("""
                MATCH (n:Disease{name: $disease_name}) 
                RETURN n.drugs AS drugs, 
                    n.description AS description, 
                    n.risk_factors AS risks,
                    n.symptoms AS symptoms
            """, disease_name = disease_name)

            value = result.single()
            if value != None:
                list = value.values(
                    "description", 
                    "symptoms",
                    "risks", 
                    "drugs"
                )
                return {
                    'description': list[0],
                    'symptoms': list[1],
                    'risks': list[2],
                    'drugs': list[3],
                }
            else:
                return None

        session = self.driver.session()
        result = session.execute_read(get_detail_by_disease, disease_name = disease_name)
        session.close()

        return result


