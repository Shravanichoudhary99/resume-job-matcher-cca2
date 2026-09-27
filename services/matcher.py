def match_skills(resume_skills, job_skills):
    resume_set = set()

    for skills in resume_skills.values():
        for skill in skills:
            resume_set.add(skill.lower())

    job_set = set()

    for skills in job_skills.values():
        for skill in skills:
            job_set.add(skill.lower())

    matched = resume_set.intersection(job_set)
    missing = job_set - resume_set

    if len(job_set) == 0:
        match_percentage = 0
    else:
        match_percentage = (len(matched) / len(job_set)) * 100

    return {
        "matched": sorted(matched),
        "missing": sorted(missing),
        "match_percentage": round(match_percentage, 2)
    }