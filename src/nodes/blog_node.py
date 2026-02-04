from pyexpat.errors import messages

from src.states.blogstate import BlogState
from langchain_core.messages import SystemMessage, HumanMessage
from src.states.blogstate import Blog

class BlogNode:

    def __init__(self,llm):
        self.llm=llm

    def title_creation(self,state:BlogState):
        """
        create the title for the blog
        :param state:
        :return:
        """
        if "topic" in state and state["topic"]:
            prompt="""
            you are an expert blog content writer. Use Markdowm formatting.
            Generate a blog title for the {topic}. This title should be creative and SEO friendly
            
            
            """
            system_message=prompt.format(topic=state["topic"])
            response= self.llm.invoke(system_message)
            return {"blog":{"title":response.content}}

    def content_generation(self,state:BlogState):
        if "topic" in state and state["topic"]:
            system_prompt= """
            you are an expert blog content writer. Use Markdowm formatting.
            Generate a detailed blog content with breakdown for the {topic}. This title should be creative and SEO friendly
            
            """
            system_message=system_prompt.format(topic=state["topic"])
            response= self.llm.invoke(system_message)
            return {"blog":{"title":state['blog']['title'],"content":response.content}}

    def translation(self, state: BlogState):
        """
        Translate the blog content to the specified language
        and return as a BlogState object.
        """
        translation_prompt = f"""
    You are a translation assistant.

    Translate the following blog into **{state["current_language"]}**.
    Ensure that **every part** of the output is in {state["current_language"]}, including headings, lists, and descriptions.

    Return the output as a JSON object with exactly these fields:
    - title: translated blog title
    - content: translated blog content

    ORIGINAL TITLE:
    {state['blog']['title']}

    ORIGINAL CONTENT:
    {state['blog']['content']}
    """

        message = [HumanMessage(translation_prompt)]
        translation_content = self.llm.with_structured_output(Blog).invoke(message)

        # return updated state
        return {
            **state,
            "blog": {
                "title": translation_content.title,
                "content": translation_content.content,
            }
        }

    # def translation(self, state: BlogState):
    #     """
    #     Transalaet the contet to the specified language
    #     """
    #     translation_prompt = """
    #     Translate the following content into {current_language}.
    #     - Maintain the original tone, style and formatting.
    #     - Adapt cultural refrences and idioms to be appropriate for {current_language}
    #
    #     ORIGINAL CONTENT:
    #     {blog_content}
    #
    #     """
    #
    #     blog_content = state["blog"]["content"]
    #     message = [
    #         HumanMessage(
    #             translation_prompt.format(current_language=state["current_language"], blog_content=blog_content))
    #
    #     ]
    #     translation_content=self.llm.with_structured_output(Blog).invoke(message)
    #
    #     return translation_content

    def route(self, state: BlogState):
        return {"current_language": state["current_language"]}


    def route_decision(self, state: BlogState):
        lang = state.get("current_language")
        print(f"DEBUG route_decision: current_language={lang!r}")
        if lang == "hindi":
            return "hindi_translation"
        if lang == "french":
            return "french_translation"
        return lang

