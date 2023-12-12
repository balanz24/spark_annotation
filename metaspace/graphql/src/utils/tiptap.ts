import { UserError } from 'graphql-errors'

export const isValidTiptapJson = (doc: string) => {
  try {
    // The tiptap library can't validate JSON without having the full set of extensions configured, which seems like
    // too much complexity to drag into graphql just for validation.
    // It should be good enough to check that the field is valid JSON, and looks like it was created by tiptap.
    const obj = JSON.parse(doc)
    return obj.type === 'doc' && obj.content != null
  } catch {
    return false
  }
}

export const validateTiptapJson = (doc: string, fieldName: string) => {
  if (!isValidTiptapJson(doc)) {
    throw new UserError(`Invalid "${fieldName}" value. This field must be in tiptap rich-text format`)
  }
}
