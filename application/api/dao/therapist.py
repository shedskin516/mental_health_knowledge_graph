from api.exceptions.notfound import NotFoundException

class TherapistDAO:
    """
    The constructor expects an instance of the Neo4j Driver, which will be
    used to interact with Neo4j.
    """
    def __init__(self, driver):
        self.driver = driver


    # get therapists by condition
    def getTherapist(self, requestData):
        def get_therapist(tx, requestData):

            result = tx.run("""
                MATCH(t)-[r1:HAS_SPECIALTY]->()-[r2:SAME_AS]->(d:Disease{name: $requestData.disease}) 
                WHERE (($requestData.modality <> '' AND t.modality CONTAINS $requestData.modality) 
                    or $requestData.modality = '')
                AND (($requestData.community <> '' AND t.communities CONTAINS $requestData.community) 
                    or $requestData.community = '')
                AND (($requestData.age <> '' AND t.age_bracket CONTAINS $requestData.age) 
                    or $requestData.age = '')
                AND (($requestData.therapy <> '' AND t.therapy_type CONTAINS $requestData.therapy) 
                    or $requestData.therapy = '')
                RETURN DISTINCT t
            """, requestData = requestData)

            res = []
            for person in result:
                node = person['t']
                obj = {
                    'name': node['name'],
                    'title': node['title'],
                    'address': node['address'],
                    'mobile': node['mobile'],
                    'specialities': node['specialities'],
                    'age': node['age_bracket'],
                    'modality': node['modality'],
                    'community': node['communities'],
                    'therapyType': node['therapy_type'],
                    'about': node['about'],
                    'website': node['website'],
                    'geo': node['geo_location']
                }
                res.append(obj)
            print('The number of therapist is ',len(res))
            return res

        session = self.driver.session()
        result = session.execute_read(get_therapist, requestData = requestData)
        session.close()

        return result


    # recommend therapists
    def recommendTherapist(self, issues):
        print(issues)
        def recommend_therapist(tx, issues):
            result = tx.run("""
                MATCH(t:Therapist)
                WHERE t.specialities CONTAINS $issues[0]
                    AND t.specialities CONTAINS $issues[1]
                    AND t.specialities CONTAINS $issues[2]
                RETURN t
            """, issues = issues)

            res = []
            for person in result:
                node = person['t']
                obj = {
                    'name': node['name'],
                    'title': node['title'],
                    'address': node['address'],
                    'mobile': node['mobile'],
                    'specialities': node['specialities'],
                    'age': node['age_bracket'],
                    'modality': node['modality'],
                    'community': node['communities'],
                    'therapyType': node['therapy_type'],
                    'about': node['about'],
                    'website': node['website'],
                    'geo': node['geo_location']
                }
                res.append(obj)
            print('The number of therapist is ',len(res))
            return res

        session = self.driver.session()
        result = session.execute_read(recommend_therapist, issues = issues)
        session.close()

        return result