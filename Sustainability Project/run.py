from function import myClass

def main():
    prompt = """This task requires you to assess a sustainability report's compliance with the requirements of Sustainability Reporting Standards.
    You will be presented with:
    1) The extract of the relevant section of the report in <Report></Report> tags that should be assessed for compliance with the requirements.
    2) Sustainability requirement that the report needs to comply with. These are presented in <Requirement></Requirement> tags.
    3) The instructions for the assessment in <Instructions></Instructions> tags.

    <Instructions>
    1) Quote the section or sections of the text that best meet the requirement, present this under the heading ""Extract from Report"".
    3) Provide short and concise recommendations on how to improve the clarity or accuracy of the report to better meet the requirement. Structure these under the heading ""Recommendations"", present them as numbered points in order of priority (most important first).
    4) If you cannot identify any text that meets the requirement then only state ""No text found that meets the requirement"" and nothing else.
    </Instructions>
    <Requirement>
    The entity should conduct non sustainability report.
    </Requirement>
    <Report>
    Citi’s full Board of Directors has ultimate oversight of Citi’s approaches to considering, evaluating and integrating climate-related risks and opportunities throughout the organization, including oversight of our Net Zero Plan.
    The Board receives regular reports from key personnel regarding climate-related matters. Since 2021, the Board has received four reports regarding Citi’s Net Zero Plan and progress towards Citi’s climate-related goals. The Board also received a climate risk and net zero deep-dive tutorial from the Chief Sustainability Officer (CSO), Global Head of Climate Risk and the Global Head of Corporate Banking.
    Three Board-level committees also have direct oversight responsibility for climate-related activities: the Nomination, Governance and Public Affairs Committee (NGPAC), the Risk Management Committee (RMC) and the Audit Committee (AC).
    The NGPAC oversees many of Citi’s ESG activities, including receiving reports from and advising management on climate-related matters. The NGPAC receives reports from Citi’s Chief Sustainability Officer on at least an annual basis. The NGPAC also reviews Citi’s policies, programs and disclosure approach for sustainability and climate change issues, and oversees management’s engagement with investors and major external stakeholders on sustainability and climate change matters. Since 2021, the NGPAC has received a number of meetings to review shareholder proposals (including ones related to fossil fuel financing and biodiversity) and received an ESG update in 2022. For more information on the roles and responsibilities of the NGPAC, please see our NGPAC Charter.
    The RMC provides oversight of Citi’s risk management framework and reviews Citi’s key risk policies and practices, including those focused on climate-related risks. The RMC also receives updates, as necessary and appropriate, from management on climate-related risk. During 2022, the RMC received updates on climate risk including the climate risk management framework, client-level climate assessment methodology and results of climate scenario analysis. For more information on the roles and responsibilities of the RMC, please see our RMC Charter.
    The AC assists the Board in fulfilling its oversight responsibilities, such as general compliance with legal and regulatory requirements and our internal disclosure controls and procedures. Ultimately, the AC has oversight over the controls and procedures related to Citi’s ESG and climate-related reporting, including both voluntary disclosures and regulatory filings. In 2022, the AC held two meetings to review existing ESG disclosure controls and procedures. For more information on the roles and responsibilities of the AC, please see our AC Charter.
    Details regarding our Board’s and Board committee’s oversight of climate matters, including the scope of the NGPAC’s oversight of Citi’s climate activities and performance and the RMC’s oversight of risk policies and frameworks, are described in greater detail in our prior TCFD Reports and in these committees’ charters on our website.
    </Report>"""

    prompt1 = """This task requires you to assess a sustainability report's compliance with the requirements of Sustainability Reporting Standards.
    You will be presented with:
    1) The extract of the relevant section of the report in <Report></Report> tags that should be assessed for compliance with the requirements.
    2) Sustainability requirement that the report needs to comply with. These are presented in <Requirement></Requirement> tags.
    3) The instructions for the assessment in <Instructions></Instructions> tags.

    <Instructions>
    1) Quote the section or sections of the text that best meet the requirement, present this under the heading ""Extract from Report"".
    3) Provide short and concise recommendations on how to improve the clarity or accuracy of the report to better meet the requirement. Structure these under the heading ""Recommendations"", present them as numbered points in order of priority (most important first).
    4) If you cannot identify any text that meets the requirement then state ""No text found that meets the requirement"".
    </Instructions>
    <Requirement>
    The objective of climate-related financial disclosures on governance is to enable users of general purpose financial reports to understand the governance processes, controls and procedures an entity uses to monitor, manage and oversee climate-related risks and opportunities. To achieve this objective, an entity shall disclose information about:

    (a) the governance body(s) (which can include a board, committee or equivalent body charged with governance) or individual(s) responsible for oversight of climate-related risks and opportunities. Specifically, the entity shall identify that body(s) or individual(s) and disclose information about:

    how the body(s) or individual(s) oversees the setting of targets related to climate-related risks and opportunities, and monitors progress towards those targets, including whether and how related performance metrics are included in remuneration policies.
    </Requirement>
    <Report>
    Citi’s full Board of Directors has ultimate oversight of Citi’s approaches to considering, evaluating and integrating climate-related risks and opportunities throughout the organization, including oversight of our Net Zero Plan.
    The Board receives regular reports from key personnel regarding climate-related matters. Since 2021, the Board has received four reports regarding Citi’s Net Zero Plan and progress towards Citi’s climate-related goals. The Board also received a climate risk and net zero deep-dive tutorial from the Chief Sustainability Officer (CSO), Global Head of Climate Risk and the Global Head of Corporate Banking.
    Three Board-level committees also have direct oversight responsibility for climate-related activities: the Nomination, Governance and Public Affairs Committee (NGPAC), the Risk Management Committee (RMC) and the Audit Committee (AC).
    The NGPAC oversees many of Citi’s ESG activities, including receiving reports from and advising management on climate-related matters. The NGPAC receives reports from Citi’s Chief Sustainability Officer on at least an annual basis. The NGPAC also reviews Citi’s policies, programs and disclosure approach for sustainability and climate change issues, and oversees management’s engagement with investors and major external stakeholders on sustainability and climate change matters. Since 2021, the NGPAC has received a number of meetings to review shareholder proposals (including ones related to fossil fuel financing and biodiversity) and received an ESG update in 2022. For more information on the roles and responsibilities of the NGPAC, please see our NGPAC Charter.
    The RMC provides oversight of Citi’s risk management framework and reviews Citi’s key risk policies and practices, including those focused on climate-related risks. The RMC also receives updates, as necessary and appropriate, from management on climate-related risk. During 2022, the RMC received updates on climate risk including the climate risk management framework, client-level climate assessment methodology and results of climate scenario analysis. For more information on the roles and responsibilities of the RMC, please see our RMC Charter.
    The AC assists the Board in fulfilling its oversight responsibilities, such as general compliance with legal and regulatory requirements and our internal disclosure controls and procedures. Ultimately, the AC has oversight over the controls and procedures related to Citi’s ESG and climate-related reporting, including both voluntary disclosures and regulatory filings. In 2022, the AC held two meetings to review existing ESG disclosure controls and procedures. For more information on the roles and responsibilities of the AC, please see our AC Charter.
    Details regarding our Board’s and Board committee’s oversight of climate matters, including the scope of the NGPAC’s oversight of Citi’s climate activities and performance and the RMC’s oversight of risk policies and frameworks, are described in greater detail in our prior TCFD Reports and in these committees’ charters on our website.
    </Report>
    """
    print("The result for the first prompt :\n")
    result = myClass.enter_prompt(prompt)
    print(result)
    print("The result for the second prompt :\n")
    result1 = myClass.enter_prompt(prompt1)
    print(result1)

if __name__ == "__main__":
    main()