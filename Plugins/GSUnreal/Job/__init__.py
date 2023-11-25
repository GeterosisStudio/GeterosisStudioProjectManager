"""This package contains a set of functions designed to run automatically in Unreal Engine. Rules for adding new features Each
work function must have its own module with and be named like this module because the program that does the work and
takes parameters: program type function to execute. """

"""
:param program: program for job
:param job: function to execute
:return: execution status and supporting information
"""

"""
Example:
job(unreal, test(param)) - run GSUnreal.Job.test.test(param)
"""